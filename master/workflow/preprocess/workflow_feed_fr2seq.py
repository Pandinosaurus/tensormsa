from master.workflow.preprocess.workflow_pre import WorkFlowPre

class WorkflowFeedFr2Seq(WorkFlowPre):
    """

    """

    def __init__(self, key = None):
        """
        init key variable
        :param key:
        :return:
        """
        self.key = key
        self._set_essence_parms(['encode_column', 'decode_column', 'max_sentence_len','preprocess'])
        self._set_update_prohibited_ids(['encode_column', 'decode_column', 'max_sentence_len','preprocess'])

    def get_encode_column(self):
        """

        :param node_id:
        :return:
        """
        if('conf' not in self.__dict__) :
            self.conf = self.get_view_obj(self.key)
        return self.conf['encode_column']

    def get_decode_column(self):
        """

        :param node_id:
        :return:
        """
        if('conf' not in self.__dict__) :
            self.conf = self.get_view_obj(self.key)
        return self.conf['decode_column']

    def get_sent_max_len(self):
        """

        :param node_id:
        :return:
        """
        if('conf' not in self.__dict__) :
            self.conf = self.get_view_obj(self.key)
        return self.conf['max_sentence_len']

    def get_preprocess_type(self):
        """

        :param node_id:
        :return:
        """
        if('conf' not in self.__dict__) :
            self.conf = self.get_view_obj(self.key)
        return self.conf['preprocess']