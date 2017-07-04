from chatbot import models
from django.core import serializers as serial
import json
from chatbot.common.chat_knowledge_mem_dict import ChatKnowledgeMemDict

class ChatKnowledgeDataDict:

    def __init__(self, cb_id):
        self.cb_id = cb_id

        #TODO : need to get data from cache
    # def get_intent_entity_keys(self):
    #     query_set = models.CB_ENTITY_LIST_INFO.objects.filter(cb_id = self.cb_id, entity_type = 'key')
    #     query_set = serial.serialize("json", query_set)
    #     return json.loads(query_set)[0]['fields']['entity_list']['key'] # list type
    #
    # def get_entity_values(self):
    #     query_set = models.CB_ENTITY_LIST_INFO.objects.filter(cb_id = self.cb_id, entity_type = 'key_values')
    #     query_set = serial.serialize("json", query_set)
    #     return json.loads(query_set)[0]['fields']['entity_list'] # json type
    #
    # def get_essential_entity(self, intent):
    #     query_set = models.CB_ENTITY_LIST_INFO.objects.filter(cb_id = self.cb_id,intent_id = intent, entity_type = 'essential')
    #     if (query_set == '[]'):
    #         return None
    #     else:
    #         query_set = serial.serialize("json", query_set)
    #         return json.loads(query_set)[0]['fields']['entity_list']['essential']  # list type
    #
    # def get_custom_entity(self):
    #     query_set = models.CB_ENTITY_LIST_INFO.objects.filter(cb_id = self.cb_id, entity_type = 'custom')
    #     query_set = serial.serialize("json", query_set)
    #     return json.loads(query_set)[0]['fields']['entity_list']['custom']  # list type

    def get_proper_tagging(self):
        query_set = models.CB_TAGGING_INFO.objects.filter(cb_id = self.cb_id)
        query_set = serial.serialize("json", query_set)
        return json.loads(query_set)[0]['fields']['proper_noun'] #JSON Type

    def get_intent_conf(self):
        query_set = models.CB_INTENT_LIST_INFO.objects.filter(cb_id = self.cb_id)
        query_set = serial.serialize("json", query_set)
        return json.loads(query_set)

    def initialize(self, cb_id):
        """
        initialize ChatKnowlodgeMemdict Class 
        :return: none
        """
        try :
            if(self.check_dict(cb_id)) :
                self.proper_key_list = sorted(self.get_proper_tagging().keys(),
                                              key=lambda x: self.get_proper_tagging()[x][0],
                                              reverse=True)
                self.proper_noun = self.get_proper_tagging()
                ChatKnowledgeMemDict.data[cb_id] = {}
                for key in self.proper_key_list :
                    ChatKnowledgeMemDict.data[cb_id][key] = self._get_entity_values(key)
        except Exception as e :
            raise Exception ("error on chatbot dict init : {0}".format(e))

    def check_dict(self, cb_id):
        """
        check if data is already loaded 
        :return: boolean
        """
        if(len(list(ChatKnowledgeMemDict.data.keys())) <= 0 ) :
            return True
        if(cb_id in ChatKnowledgeMemDict.data.keys()) :
            return False
        else :
            return True

    def _get_entity_values(self, key):
        try :
            values = []
            with open(self.proper_noun.get(key)[1], 'r') as input_file :
                if(input_file is not None):
                    for line in input_file.read().splitlines():
                        values.append(line)
            return values
        except Exception as e :
            raise Exception (e)

    def get_intent_uuid(self):
        query_set = models.CB_INTENT_LIST_INFO.objects.filter(cb_id = self.cb_id)
        query_set = serial.serialize("json", query_set)
        return json.loads(query_set)

    def get_entity_uuid(self):
        query_set = models.CB_ENTITY_RELATION_INFO.objects.filter(cb_id = self.cb_id)
        query_set = serial.serialize("json", query_set)
        return json.loads(query_set)
