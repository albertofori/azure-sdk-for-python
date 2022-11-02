# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_execute_request(location_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-03-08-preview")
    )  # type: Literal["2022-03-08-preview"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.DBforPostgreSQL/locations/{locationName}/checkNameAvailability",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "locationName": _SERIALIZER.url("location_name", location_name, "str", min_length=1, pattern=r"^[-\w\._]+$"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class CheckNameAvailabilityWithLocationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.rdbms.postgresql_flexibleservers.PostgreSQLManagementClient`'s
        :attr:`check_name_availability_with_location` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def execute(
        self,
        location_name: str,
        name_availability_request: _models.CheckNameAvailabilityRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailability:
        """Check the availability of name for resource.

        :param location_name: The name of the location. Required.
        :type location_name: str
        :param name_availability_request: The required parameters for checking if resource name is
         available. Required.
        :type name_availability_request:
         ~azure.mgmt.rdbms.postgresql_flexibleservers.models.CheckNameAvailabilityRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailability or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.postgresql_flexibleservers.models.NameAvailability
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def execute(
        self,
        location_name: str,
        name_availability_request: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailability:
        """Check the availability of name for resource.

        :param location_name: The name of the location. Required.
        :type location_name: str
        :param name_availability_request: The required parameters for checking if resource name is
         available. Required.
        :type name_availability_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailability or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.postgresql_flexibleservers.models.NameAvailability
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def execute(
        self,
        location_name: str,
        name_availability_request: Union[_models.CheckNameAvailabilityRequest, IO],
        **kwargs: Any
    ) -> _models.NameAvailability:
        """Check the availability of name for resource.

        :param location_name: The name of the location. Required.
        :type location_name: str
        :param name_availability_request: The required parameters for checking if resource name is
         available. Is either a model type or a IO type. Required.
        :type name_availability_request:
         ~azure.mgmt.rdbms.postgresql_flexibleservers.models.CheckNameAvailabilityRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailability or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.postgresql_flexibleservers.models.NameAvailability
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-03-08-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.NameAvailability]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(name_availability_request, (IO, bytes)):
            _content = name_availability_request
        else:
            _json = self._serialize.body(name_availability_request, "CheckNameAvailabilityRequest")

        request = build_execute_request(
            location_name=location_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.execute.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("NameAvailability", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    execute.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.DBforPostgreSQL/locations/{locationName}/checkNameAvailability"}  # type: ignore