from time import gmtime, strftime, time, strptime
from math import floor
SUFFIX = '99CEN'
ENDLINE = '...<cr>'
PART_SEG = '|'

class hl7_segment:
	def to_str(self):
		pass
	@staticmethod
	def time_str(tempo):
		return strftime("%Y%m%d%H%M%S", tempo)

class msh(hl7_segment):
	def __init__(self,seps,placer,filler, event_type, htime = None):
		self.seps = seps
		self.placer = placer
		self.filler = filler
		self.event_type = event_type
		if htime:
			self.htime = htime
		else:
			self.htime = gmtime()
	def to_str(self):
		return "MSH|%s|%s||%s|%s||%s|%s" % (self.seps, self.placer[1],
		self.filler[1], hl7_segment.time_str(self.htime), self.event_type, ENDLINE)
	@staticmethod
	def generate(parts):
		return msh(parts[1], (0,parts[2]), (0,parts[3]), parts[5], strptime(parts[4], "%Y%m%d%H%M%S"))
	
class pid(hl7_segment):
	def __init__(self, seq_num, ide, name):
		self.seq_num = seq_num
		self.ide = ide
		self.name = name
	def to_str(self):
		return "PID|%d||%d||%s|%s" % (self.seq_num, self.ide, 
		self.name,ENDLINE)
	@staticmethod
	def generate(parts):
		return pid(int(parts[1]),int(parts[2]),parts[3])

class obr(hl7_segment):
	def __init__(self, seq_num, placer, filler, cod):
		self.seq_num = seq_num
		self.placer = placer
		self.filler = filler
		self.cod = cod
	def to_str(self):
		return "OBR|%d|%s^%s|%s^%s|%d^%s^%s|%s" % (self.seq_num,
		self.placer[0], self.placer[1], self.filler[0], self.filler[1],
		self.cod, measure.cods[self.cod], SUFFIX,ENDLINE)
	@staticmethod
	def generate(parts):
		subparts1 = parts[2].split('^')
		subparts2 = parts[3].split('^')
		subparts3 = parts[4].split('^')
		return obr(int(parts[1]),(subparts1[0],subparts1[1]),(subparts2[0],subparts2[1]), int(subparts3[0]))

class obx(hl7_segment):
	def __init__(self, seq_num, obx_type, cod, obx_subtype, chn_number, data):
		self.seq_num = seq_num
		self.obx_type = obx_type
		self.cod = cod
		self.obx_subtype = obx_subtype
		self.chn_number = chn_number
		self.data = data
	
	def to_str(self):
		return "OBX|%d|%s|%d&%s^^%s|%d|%s|%s" % (self.seq_num,
		self.obx_type, self.cod, self.obx_subtype, SUFFIX, 
		self.chn_number, self.data,ENDLINE)
		
	def fill_chn_df(self, chn):
		parts = self.data.split('^')
		parts.remove('')
		chn.numero = int(parts[0])
		chn.descricao = parts[1]
		subparts = parts[2].split('&')
		chn.resolucao = float(subparts[0])
		chn.unidade = subparts[1]
		chn.fs = int(parts[3])
		subparts = parts[4].split('&')
		chn.limites = (int(subparts[0]), int(subparts[1]))
	
	def fill_chn_data(self, chn):
		parts = self.data.split('^')
		if '' in parts:
			parts.remove('')
		chn.bind_data(map(lambda x: int(x), parts))
		
	@staticmethod
	def generate(parts):
		subparts = parts[3].split('^')
		gparts = subparts[0].split('&')
		return obx(int(parts[1]), parts[2], int(gparts[0]), gparts[1], int(parts[4]), parts[5])

class measure:
	def __init__(self, cod = 6, chans = None):
		if chans:
			self.channels = chans
		else:
			self.channels = []
		self.cod = cod
	def add_channel(self, chan):
		self.channels.append(chan)
		
	cods = {1:'Temperature', 2:'Invasive pressure',
	 3:'Non-invasive pressure', 4:'Oximetry', 5:'Cardiac Frequency',
	 6:'ECG'}
	
class channel:
	def __init__(self, numero = None, descricao = None, resolucao = None, unidade = None, fs = None, limites = None, gen = None):
		self.numero = numero
		self.descricao = descricao
		self.resolucao = resolucao
		self.unidade = unidade
		self.fs = fs
		self.limites = limites
		self.gen = gen
	def bind_data(self, data):
		self.data = data
		self.data_time_str = hl7_segment.time_str(gmtime()) + ".%03.0f" % ((time() - floor(time()))*1000)
	def def_str(self):
		return "%d^%s^%.3f&%s^^%d^%d&%d" % (self.numero, self.descricao, self.resolucao, self.unidade, self.fs, self.limites[0], self.limites[1])
	def time_str(self):
		return self.data_time_str
	def data_str(self):
		dt_str = ""
		for datum in self.data:
			#if datum == self.data[-1]:
				#dt_str += ("%s" % datum)
			#else:
			dt_str += ("%s^" % datum)
		return dt_str
		
class patient:
	def __init__(self, ide = None, name = None):
		self.ide = ide
		self.name = name
		self.measures = []
		
	def add_measure(self, measure):
		self.measures.append(measure)

class oru_wav:
	def __init__(self,placer = None,filler = None):
		self.segments = []
		self.placer = placer
		self.filler = filler
		self.patients = []
		
	def fill_segments(self):
		header = msh('^~\&', self.placer, self.filler,'ORU^W01^ORU_R01')
		self.segments.append(header)
		cont_p = 0
		for pat in self.patients:
			cont_p += 1
			pat_pid = pid(cont_p, pat.ide, pat.name)
			self.segments.append(pat_pid)
			cont_m = 0
			for mea in pat.measures:
				cont_m += 1
				measure_obr = obr(cont_m, self.placer, self.filler, mea.cod)
				self.segments.append(measure_obr)
				cont_ch = 0
				for chn in mea.channels:
					cont_ch += 1
					ch_def_obx = obx(3*cont_ch - 2, 'CD', mea.cod, 'CHN', chn.numero, chn.def_str())
					self.segments.append(ch_def_obx)
					ch_time_obx = obx(3*cont_ch - 1, 'DTM', mea.cod, 'TIM', chn.numero, chn.time_str())
					self.segments.append(ch_time_obx)
					ch_data_obx = obx(3*cont_ch, 'NA', mea.cod, 'WAV', chn.numero, chn.data_str())
					self.segments.append(ch_data_obx)
				
	def add_patient(self, patient):
		self.patients.append(patient)
	
	def to_str(self):
		oru_str = ''
		for segment in self.segments:
			oru_str += segment.to_str()
		return oru_str
		
	def __str__(self):
		return self.to_str().replace(ENDLINE,'\n')
		
	

class hl7_segment_factory:
	types = {'MSH':msh, 'OBX':obx, 'PID':pid, 'OBR':obr}
	@staticmethod
	def create_segment(str_segment):
		parts = str_segment.split(PART_SEG)
		parts = filter(lambda p: p != '', parts)
		segment = hl7_segment_factory.types[parts[0]].generate(parts)
		return segment

class oru_wav_factory:
	@staticmethod
	def create_oru(msg_str):
		str_segments = msg_str.split(ENDLINE)
		#str_segments.remove('')
		m_oru = oru_wav()
		for str_seg in str_segments:
			if str_seg != '':
				seg = hl7_segment_factory.create_segment(str_seg)
				m_oru.segments.append(seg)
		m_oru.placer = m_oru.segments[2].placer
		m_oru.filler = m_oru.segments[2].filler
		return m_oru
		
class patient_factory:
	@staticmethod
	def create_patient(segments):
		pat = patient()
		curr_msr = None
		curr_chn = None
		for seg in segments:
			if isinstance(seg, pid):
				pat.ide = seg.ide
				pat.name = seg.name
			elif isinstance(seg, obr):
				curr_msr = measure(seg.cod)
				pat.add_measure(curr_msr) 
			elif isinstance(seg, obx):
				if seg.obx_type == 'CD':
					curr_chn = channel()
					curr_msr.add_channel(curr_chn)
					seg.fill_chn_df(curr_chn)
				elif seg.obx_type == 'DT':
					curr_chn.data_time_str = seg.data
				elif seg.obx_type == 'NA':
					seg.fill_chn_data(curr_chn)
		return pat
					
if __name__ == '__main__':
	p1 = patient(1,'Jonas Brothers')
	m1 = measure()
	p1.add_measure(m1)
	chn1 = channel(1, 'D1', 0.5, 'mv', 1000, (-1024,1023))
	m1.add_channel(chn1)
	chn1.bind_data(range(0,40))
	chn2 = channel(2, 'D2', 0.5, 'mv', 1000, (-1024,1023))
	m1.add_channel(chn2)
	chn2.bind_data(range(-30,10))
	orw1 = oru_wav((12312,'CEN'), (12354,'MON'))
	orw1.add_patient(p1)
	orw1.fill_segments()
	print orw1
	orw2 = oru_wav_factory.create_oru(orw1.to_str())
	print '-------------------------\n'
	print orw2
	p2 = patient_factory.create_patient(orw2.segments)
	print p2.measures[0].channels[1].data
	
	
