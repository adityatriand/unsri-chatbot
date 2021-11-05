from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class JumlahJurusanFakultas(Action):

	def name(self) -> Text:
		return "action_jumlah_jurusan_fakultas"


	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		for x in tracker.latest_message['entities']:
			name = ''
			if(x['entity']=='nama_fakultas'):
				name = x['value']
				if (name == 'fakultas ekonomi' or name == 'FE'or name=='fe'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_ekonomi")
				elif(name== 'fakultas hukum'or name == 'FH' or name == 'fh'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_hukum")
				elif(name == 'fakultas teknik' or name == 'FT' or name == 'ft'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_teknik")
				elif (name == 'fakultas kedokteran' or name == 'FK' or name=='fk'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_kedokteran")
				elif (name == 'fakultas pertanian' or name == 'FP' or name=='fp'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_pertanian")
				elif(name == 'fakultas keguruan dan ilmu pendidikan' or name == 'FKIP' or name=='fkip'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_keguruan")
				elif (name == 'fakultas ilmu sosial dan ilmu politik' or name == 'FISIP' or name=='fisip'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_ilmu_sosial_dan_ilmu_politik")
				elif (name == 'fakultas matematika dan ilmu pengetahuan' or name == 'FMIPA' or name=='fmipa'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_matematika_dan_ilmu_pengetahuan")
				elif (name == 'fakultas ilmu komputer' or name == 'FASILKOM' or name=='fasilkom'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_ilmu_komputer")
				elif (name == 'fakultas kesehatan masyarakat' or name == 'FKM' or name=='fkm'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_fakultas_kesehatan_masyarakat")
				elif (name == 'program pascasarjana'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_program_pascasarjana")
				elif (name == 'program profesi'):
					dispatcher.utter_message(response="utter_faq/ask_jumlah_jurusan_program_profesi")
				else:
					dispatcher.utter_message(response="utter_minus_param")
			else:
				dispatcher.utter_message(response="utter_respon_failed")
		return []

class JurusanFakultas(Action):

	def name(self) -> Text:
		return "action_jurusan_fakultas"


	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		for x in tracker.latest_message['entities']:
			name = ''
			if(x['entity']=='nama_fakultas'):
				name = x['value']
				if (name == 'fakultas ekonomi' or name == 'FE'or name=='fe'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_ekonomi")
				elif(name== 'fakultas hukum'or name == 'FH' or name == 'fh'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_hukum")
				elif(name == 'fakultas teknik' or name == 'FT' or name == 'ft'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_teknik")
				elif (name == 'fakultas kedokteran' or name == 'FK' or name=='fk'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_kedokteran")
				elif (name == 'fakultas pertanian' or name == 'FP' or name=='fp'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_pertanian")
				elif(name == 'fakultas keguruan dan ilmu pendidikan' or name == 'FKIP' or name=='fkip'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_keguruan")
				elif (name == 'fakultas ilmu sosial dan ilmu politik' or name == 'FISIP' or name=='fisip'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_ilmu_sosial_dan_ilmu_politik")
				elif (name == 'fakultas matematika dan ilmu pengetahuan' or name == 'FMIPA' or name=='fmipa'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_matematika_dan_ilmu_pengetahuan")
				elif (name == 'fakultas ilmu komputer' or name == 'FASILKOM' or name=='fasilkom'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_ilmu_komputer")
				elif (name == 'fakultas kesehatan masyarakat' or name == 'FKM' or name=='fkm'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_fakultas_kesehatan_masyarakat")
				elif (name == 'program pascasarjana'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_program_pascasarjana")
				elif (name == 'program profesi'):
					dispatcher.utter_message(response="utter_faq/ask_jurusan_program_profesi")
				else:
					dispatcher.utter_message(response="utter_minus_param")
			else:
				dispatcher.utter_message(response="utter_respon_failed")
		return []

class WakilRektor(Action):

	def name(self) -> Text:
		return "action_wakil_rektor"


	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		for x in tracker.latest_message['entities']:
			if(x['entity']=='posisi_wakil'):
				name = x['value']
				if (name == 'pertama' or name == 'I'):
					dispatcher.utter_message(response="utter_faq/ask_wakil_rektor_I")
				elif (name == 'kedua' or name == 'II'):
					dispatcher.utter_message(response="utter_faq/ask_wakil_rektor_II")
				elif (name == 'ketiga' or name == 'III'):
					dispatcher.utter_message(response="utter_faq/ask_wakil_rektor_III")
				elif (name == 'keempat' or name == 'IV'):
					dispatcher.utter_message(response="utter_faq/ask_wakil_rektor_IV")
				else:
					dispatcher.utter_message(response="utter_respon_failed")
			else:
				dispatcher.utter_message(response="utter_minus_param")
		return []

class ResponJawaban(Action):

	def name(self) -> Text:
		return "action_respon_jawaban"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		for x in tracker.latest_message['entities']:
			if(x['entity']=='respon'):
				name = x['value']
				if name == 'iya':
					dispatcher.utter_message(response="utter_chitchat/happy_end_ask")
				elif name == 'tidak':
					dispatcher.utter_message(response='utter_chitchat/bad_end_ask')
				elif name == 'tanya':
					dispatcher.utter_message(text='Silahkan bertanya lagi :D')
				elif name == 'feedback':
					dispatcher.utter_message(response='utter_ask_nama')
				else:
					dispatcher.utter_message(response='utter_respon_failed')
			else:
				dispatcher.utter_message(response='utter_respon_failed')
		return []

class GetNamaUser(Action):

	def name(self) -> Text:
		return "action_nama_user"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		nama = tracker.latest_message['text']
		dispatcher.utter_message(response='utter_ask_pendapat')
		return[SlotSet("nama",nama)]

class GetPendapatUser(Action):

	def name(self) -> Text:
		return "action_pendapat_user"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		pendapat = tracker.latest_message['text']
		dispatcher.utter_message(response='utter_terima_kasih')
		return[SlotSet("pendapat",pendapat)]