import sys
import numpy as np
from Queue import Queue
sys.path.insert(0, '../geradores')
from gerador_arquivo import gerador_arquivo
from itertools import tee, islice, chain, izip
import pyqtgraph
class QRSDetector:

    def __init__(self,fs):
        self.fs = fs
        self.segmento = []
        self.mm = Queue()
        self.M = 0
        self.F = 0
        self.R = 0
        self.rr = Queue()
        self.inter_qrs = Queue()
        self.pos = []
        self.ms2n = lambda x: int(np.round((self.fs/1000.0)*x))
        self.dec = lambda ini, fim, q, x: x*(np.power(float(fim)/ini,1/float(self.ms2n(q) - 1.0)))
        self.t_qrs = self.ms2n(250)
        self.y = []
        self.t = 0
        self.rm = 10000
        self.count = 0

    def addData(self, data):
        self.segmento += data

    def addToQueue(self, queue,val):
        if len(queue.queue) > 4:
            queue.get()
        queue.put(val)

    @staticmethod
    def complexLead(ent):
        p,n = tee(ent,2)
        n = chain(islice(n,2,None),[])
        return np.abs([a - b for a, b in izip(n,p)])

    def detect(self):
        self.inter_qrs.queue.clear();
        ref = self.complexLead(self.segmento)
        self.M = 0.7*np.max(ref)
        refM = self.M
        mfrs = []
        for y in ref:
            self.y.append(y)
            self.count = len(self.y)
            MFR = self.M - self.R + self.F
            if self.t_qrs > self.ms2n(200) and y > MFR:
                self.pos.append(self.count)
                if self.count < self.ms2n(2000):
                    self.addToQueue(self.mm,refM)
                else:
                    self.addToQueue(self.mm,0.7*np.max(ref[self.count - self.ms2n(1800):self.count]))
                if len(self.pos) > 1:
                    inter = self.pos[-1] - self.pos[-2]
                    self.addToQueue(self.rr,inter)
                    self.inter_qrs.put(inter)
                    self.rm = np.mean(self.rr.queue)
                
                self.t_qrs = 0;
                self.M = np.mean(self.mm.queue)
                refM = np.mean(self.mm.queue)
                self.R = 0
                self.F = 0
                
            else:
                if self.count > self.ms2n(350):
                    pa = self.y[self.count - self.ms2n(349):self.count - self.ms2n(299)]
                    pb = self.y[self.count - self.ms2n(49):self.count]
                    self.F = self.F + (np.max(pa) - np.max(pb))/150.0
                if self.t_qrs > self.ms2n(200) and self.t_qrs < self.ms2n(1200):
                    self.M = self.dec(refM ,0.75*refM, self.ms2n(1000), self.M)
                if self.t_qrs == round((2/3.0)*self.rm):
                    self.R = 0.01*refM
                if self.t_qrs > round((2/3.0)*self.rm) and self.t_qrs < self.rm:
                    self.R = self.dec(0.01*refM, 0.10*refM, self.ms2n(1400), self.R)
            self.t_qrs += 1
            print MFR, self.M, self.F, self.R, y
            
        

    

if __name__ == '__main__':
    g = gerador_arquivo('../resources/.ecg_180',256, 10000, int)
    data = g.getNext()
    qrsdec = QRSDetector(256)
    qrsdec.addData(data)
    qrsdec.detect()
    print qrsdec.inter_qrs.queue