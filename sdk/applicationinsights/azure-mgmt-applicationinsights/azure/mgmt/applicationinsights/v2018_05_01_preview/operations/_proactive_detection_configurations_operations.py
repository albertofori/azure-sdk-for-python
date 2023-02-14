# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_group_name: str, resource_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2018-05-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2018-05-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, resource_name: str, configuration_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2018-05-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2018-05-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "ConfigurationId": _SERIALIZER.url("configuration_id", configuration_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(
    resource_group_name: str, resource_name: str, configuration_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2018-05-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2018-05-01-preview")
    )
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "ConfigurationId": _SERIALIZER.url("configuration_id", configuration_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


class ProactiveDetectionConfigurationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.applicationinsights.v2018_05_01_preview.ApplicationInsightsManagementClient`'s
        :attr:`proactive_detection_configurations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, resource_group_name: str, resource_name: str, **kwargs: Any
    ) -> List[_models.ApplicationInsightsComponentProactiveDetectionConfiguration]:
        """Gets a list of ProactiveDetection configurations of an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ApplicationInsightsComponentProactiveDetectionConfiguration or the result of
         cls(response)
        :rtype:
         list[~azure.mgmt.applicationinsights.v2018_05_01_preview.models.ApplicationInsightsComponentProactiveDetectionConfiguration]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2018-05-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2018-05-01-preview")
        )
        cls: ClsType[List[_models.ApplicationInsightsComponentProactiveDetectionConfiguration]] = kwargs.pop(
            "cls", None
        )

        request = build_list_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize(
            "[ApplicationInsightsComponentProactiveDetectionConfiguration]", pipeline_response
        )

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs"
    }

    @distributed_trace
    def get(
        self, resource_group_name: str, resource_name: str, configuration_id: str, **kwargs: Any
    ) -> _models.ApplicationInsightsComponentProactiveDetectionConfiguration:
        """Get the ProactiveDetection configuration for this configuration id.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param configuration_id: The ProactiveDetection configuration ID. This is unique within a
         Application Insights component. Required.
        :type configuration_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentProactiveDetectionConfiguration or the result of
         cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2018_05_01_preview.models.ApplicationInsightsComponentProactiveDetectionConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2018-05-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2018-05-01-preview")
        )
        cls: ClsType[_models.ApplicationInsightsComponentProactiveDetectionConfiguration] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            configuration_id=configuration_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize(
            "ApplicationInsightsComponentProactiveDetectionConfiguration", pipeline_response
        )

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId}"
    }

    @overload
    def update(
        self,
        resource_group_name: str,
        resource_name: str,
        configuration_id: str,
        proactive_detection_properties: _models.ApplicationInsightsComponentProactiveDetectionConfiguration,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationInsightsComponentProactiveDetectionConfiguration:
        """Update the ProactiveDetection configuration for this configuration id.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param configuration_id: The ProactiveDetection configuration ID. This is unique within a
         Application Insights component. Required.
        :type configuration_id: str
        :param proactive_detection_properties: Properties that need to be specified to update the
         ProactiveDetection configuration. Required.
        :type proactive_detection_properties:
         ~azure.mgmt.applicationinsights.v2018_05_01_preview.models.ApplicationInsightsComponentProactiveDetectionConfiguration
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentProactiveDetectionConfiguration or the result of
         cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2018_05_01_preview.models.ApplicationInsightsComponentProactiveDetectionConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        resource_group_name: str,
        resource_name: str,
        configuration_id: str,
        proactive_detection_properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationInsightsComponentProactiveDetectionConfiguration:
        """Update the ProactiveDetection configuration for this configuration id.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param configuration_id: The ProactiveDetection configuration ID. This is unique within a
         Application Insights component. Required.
        :type configuration_id: str
        :param proactive_detection_properties: Properties that need to be specified to update the
         ProactiveDetection configuration. Required.
        :type proactive_detection_properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentProactiveDetectionConfiguration or the result of
         cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2018_05_01_preview.models.ApplicationInsightsComponentProactiveDetectionConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        resource_name: str,
        configuration_id: str,
        proactive_detection_properties: Union[_models.ApplicationInsightsComponentProactiveDetectionConfiguration, IO],
        **kwargs: Any
    ) -> _models.ApplicationInsightsComponentProactiveDetectionConfiguration:
        """Update the ProactiveDetection configuration for this configuration id.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param configuration_id: The ProactiveDetection configuration ID. This is unique within a
         Application Insights component. Required.
        :type configuration_id: str
        :param proactive_detection_properties: Properties that need to be specified to update the
         ProactiveDetection configuration. Is either a
         ApplicationInsightsComponentProactiveDetectionConfiguration type or a IO type. Required.
        :type proactive_detection_properties:
         ~azure.mgmt.applicationinsights.v2018_05_01_preview.models.ApplicationInsightsComponentProactiveDetectionConfiguration
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentProactiveDetectionConfiguration or the result of
         cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2018_05_01_preview.models.ApplicationInsightsComponentProactiveDetectionConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2018-05-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2018-05-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ApplicationInsightsComponentProactiveDetectionConfiguration] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(proactive_detection_properties, (IO, bytes)):
            _content = proactive_detection_properties
        else:
            _json = self._serialize.body(
                proactive_detection_properties, "ApplicationInsightsComponentProactiveDetectionConfiguration"
            )

        request = build_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            configuration_id=configuration_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize(
            "ApplicationInsightsComponentProactiveDetectionConfiguration", pipeline_response
        )

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId}"
    }
