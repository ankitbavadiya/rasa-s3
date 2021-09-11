from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action


class CreateS3Bucket(FormAction):
    def name(self):
        return "s3_form"

    def required_slots(self,tracker) -> List[Text]:
        return ["access_key","secret_key","bucket_name","bucket_region"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
                "access_key": [
                    self.from_text(),
                ],
                "secret_key": [
                    self.from_text(),
                ],                
                "bucket_name": [
                    self.from_text(),
                ],
                "bucket_region": [
                    self.from_text(),
                ],
            }
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        print(tracker.current_slot_values())
                
        # dispatcher.utter_message(template="utter_submit_buy")
        dispatcher.utter_template("utter_submit_buy", tracker)    
        return []