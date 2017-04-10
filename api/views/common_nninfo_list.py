import json
from rest_framework.response import Response
from rest_framework.views import APIView
from master.network.nn_common_manager import NNCommonManager

class CommonNNInfoList(APIView):
    """
    """
    def post(self, request, nnid):
        """
        - desc : insert cnn configuration data
        """
        try:
            input_parm = request.data
            input_parm['nn_id'] = nnid
            return_data = NNCommonManager().insert_nn_info(input_parm)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def get(self, request, nnid):
        """
        - desc : get cnn configuration data
        """
        try:
            condition = {}
            condition['nn_id'] = nnid
            return_data = NNCommonManager().get_nn_info(condition)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def put(self, request, nnid):
        """
        - desc ; update cnn configuration data
        """
        try:
            input_parm = request.data
            input_parm['nn_id'] = nnid
            return_data = NNCommonManager().update_nn_info(input_parm)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def delete(self, request, nnid):
        """
        - desc : delete cnn configuration data
        """
        try:
            input_parm = request.data
            input_parm['nn_id'] = nnid
            return_data = NNCommonManager().delete_nn_info(input_parm)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))
