from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class JumlahJurusanFakultas(Action):

    def name(self) -> Text:
        return "action_jumlah_jurusan_fakultas"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    	for x in tracker.latest_message['entities']:
    		if(x['entity']=='fakultas'):
    			name = x['value']
    			if(name == 'fakultas ekonomi' || name == 'FE'):
    				dispatcher.utter_message(text="{name} masuk")

        return []

