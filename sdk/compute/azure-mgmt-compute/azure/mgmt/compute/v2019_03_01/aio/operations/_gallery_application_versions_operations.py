# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
from urllib.parse import parse_qs, urljoin, urlparse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._gallery_application_versions_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_by_gallery_application_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class GalleryApplicationVersionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2019_03_01.aio.ComputeManagementClient`'s
        :attr:`gallery_application_versions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        gallery_name: str,
        gallery_application_name: str,
        gallery_application_version_name: str,
        gallery_application_version: Union[_models.GalleryApplicationVersion, IO],
        **kwargs: Any
    ) -> _models.GalleryApplicationVersion:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GalleryApplicationVersion]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(gallery_application_version, (IO, bytes)):
            _content = gallery_application_version
        else:
            _json = self._serialize.body(gallery_application_version, "GalleryApplicationVersion")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            gallery_name=gallery_name,
            gallery_application_name=gallery_application_name,
            gallery_application_version_name=gallery_application_version_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._create_or_update_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("GalleryApplicationVersion", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("GalleryApplicationVersion", pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize("GalleryApplicationVersion", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}"}  # type: ignore

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        gallery_name: str,
        gallery_application_name: str,
        gallery_application_version_name: str,
        gallery_application_version: _models.GalleryApplicationVersion,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.GalleryApplicationVersion]:
        """Create or update a gallery Application Version.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides. Required.
        :type gallery_name: str
        :param gallery_application_name: The name of the gallery Application Definition in which the
         Application Version is to be created. Required.
        :type gallery_application_name: str
        :param gallery_application_version_name: The name of the gallery Application Version to be
         created. Needs to follow semantic version name pattern: The allowed characters are digit and
         period. Digits must be within the range of a 32-bit integer. Format:
         :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`. Required.
        :type gallery_application_version_name: str
        :param gallery_application_version: Parameters supplied to the create or update gallery
         Application Version operation. Required.
        :type gallery_application_version:
         ~azure.mgmt.compute.v2019_03_01.models.GalleryApplicationVersion
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either GalleryApplicationVersion or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2019_03_01.models.GalleryApplicationVersion]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        gallery_name: str,
        gallery_application_name: str,
        gallery_application_version_name: str,
        gallery_application_version: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.GalleryApplicationVersion]:
        """Create or update a gallery Application Version.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides. Required.
        :type gallery_name: str
        :param gallery_application_name: The name of the gallery Application Definition in which the
         Application Version is to be created. Required.
        :type gallery_application_name: str
        :param gallery_application_version_name: The name of the gallery Application Version to be
         created. Needs to follow semantic version name pattern: The allowed characters are digit and
         period. Digits must be within the range of a 32-bit integer. Format:
         :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`. Required.
        :type gallery_application_version_name: str
        :param gallery_application_version: Parameters supplied to the create or update gallery
         Application Version operation. Required.
        :type gallery_application_version: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either GalleryApplicationVersion or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2019_03_01.models.GalleryApplicationVersion]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        gallery_name: str,
        gallery_application_name: str,
        gallery_application_version_name: str,
        gallery_application_version: Union[_models.GalleryApplicationVersion, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.GalleryApplicationVersion]:
        """Create or update a gallery Application Version.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides. Required.
        :type gallery_name: str
        :param gallery_application_name: The name of the gallery Application Definition in which the
         Application Version is to be created. Required.
        :type gallery_application_name: str
        :param gallery_application_version_name: The name of the gallery Application Version to be
         created. Needs to follow semantic version name pattern: The allowed characters are digit and
         period. Digits must be within the range of a 32-bit integer. Format:
         :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`. Required.
        :type gallery_application_version_name: str
        :param gallery_application_version: Parameters supplied to the create or update gallery
         Application Version operation. Is either a model type or a IO type. Required.
        :type gallery_application_version:
         ~azure.mgmt.compute.v2019_03_01.models.GalleryApplicationVersion or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either GalleryApplicationVersion or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2019_03_01.models.GalleryApplicationVersion]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GalleryApplicationVersion]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(  # type: ignore
                resource_group_name=resource_group_name,
                gallery_name=gallery_name,
                gallery_application_name=gallery_application_name,
                gallery_application_version_name=gallery_application_version_name,
                gallery_application_version=gallery_application_version,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("GalleryApplicationVersion", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        gallery_name: str,
        gallery_application_name: str,
        gallery_application_version_name: str,
        expand: Optional[Union[str, _models.ReplicationStatusTypes]] = None,
        **kwargs: Any
    ) -> _models.GalleryApplicationVersion:
        """Retrieves information about a gallery Application Version.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides. Required.
        :type gallery_name: str
        :param gallery_application_name: The name of the gallery Application Definition in which the
         Application Version resides. Required.
        :type gallery_application_name: str
        :param gallery_application_version_name: The name of the gallery Application Version to be
         retrieved. Required.
        :type gallery_application_version_name: str
        :param expand: The expand expression to apply on the operation. "ReplicationStatus" Default
         value is None.
        :type expand: str or ~azure.mgmt.compute.v2019_03_01.models.ReplicationStatusTypes
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GalleryApplicationVersion or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2019_03_01.models.GalleryApplicationVersion
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GalleryApplicationVersion]

        request = build_get_request(
            resource_group_name=resource_group_name,
            gallery_name=gallery_name,
            gallery_application_name=gallery_application_name,
            gallery_application_version_name=gallery_application_version_name,
            subscription_id=self._config.subscription_id,
            expand=expand,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("GalleryApplicationVersion", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}"}  # type: ignore

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        gallery_name: str,
        gallery_application_name: str,
        gallery_application_version_name: str,
        **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            gallery_name=gallery_name,
            gallery_application_name=gallery_application_name,
            gallery_application_version_name=gallery_application_version_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}"}  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self,
        resource_group_name: str,
        gallery_name: str,
        gallery_application_name: str,
        gallery_application_version_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Delete a gallery Application Version.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides. Required.
        :type gallery_name: str
        :param gallery_application_name: The name of the gallery Application Definition in which the
         Application Version resides. Required.
        :type gallery_application_name: str
        :param gallery_application_version_name: The name of the gallery Application Version to be
         deleted. Required.
        :type gallery_application_version_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                gallery_name=gallery_name,
                gallery_application_name=gallery_application_name,
                gallery_application_version_name=gallery_application_version_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}"}  # type: ignore

    @distributed_trace
    def list_by_gallery_application(
        self, resource_group_name: str, gallery_name: str, gallery_application_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.GalleryApplicationVersion"]:
        """List gallery Application Versions in a gallery Application Definition.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides. Required.
        :type gallery_name: str
        :param gallery_application_name: The name of the Shared Application Gallery Application
         Definition from which the Application Versions are to be listed. Required.
        :type gallery_application_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GalleryApplicationVersion or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.compute.v2019_03_01.models.GalleryApplicationVersion]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-03-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GalleryApplicationVersionList]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_gallery_application_request(
                    resource_group_name=resource_group_name,
                    gallery_name=gallery_name,
                    gallery_application_name=gallery_application_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_gallery_application.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urlparse(next_link)
                _next_request_params = case_insensitive_dict(parse_qs(_parsed_next_link.query))
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest("GET", urljoin(next_link, _parsed_next_link.path), params=_next_request_params)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("GalleryApplicationVersionList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_gallery_application.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions"}  # type: ignore
