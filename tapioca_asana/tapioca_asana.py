# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from requests.auth import HTTPBasicAuth


from .resource_mapping import RESOURCE_MAPPING


class AsanaClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://app.asana.com/api/1.0'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(AsanaClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        
        params['auth'] = HTTPBasicAuth(api_params.get('personal_key'), '')
        

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Asana = generate_wrapper_from_adapter(AsanaClientAdapter)
