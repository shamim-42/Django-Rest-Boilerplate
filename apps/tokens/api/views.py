from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import (
    viewsets,
    serializers,
    status
)
from apps.tokens.models import *
from apps.tokens.api.serializers import *

class TokenView(viewsets.ModelViewSet):
  queryset = Token.objects.all()
  serializer_class = TokenSerializer
  # lookup_field='id'

  # for custom handling of http method 'post' override the
  # create() function and write your custom logic
  # you can find more from 'http://cdrf.co'

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    result = self.perform_create(serializer)
    response = serializer.data

    return Response(
        data={
            'status': True,
            'message': "Token stored successfully",
            'data': response
        },
        status=status.HTTP_201_CREATED
    )


  def list(self, request, *args, **kwargs):
    try:
      queryset = self.filter_queryset(self.get_queryset())

      # PAGINATION PURPOSE
      # We are setting default number of items per page = 40
      # By default we set starting index 0 and ending index 39 (index=9 means serially 10th item) [see python data slicing mechanism to know more ]
      page_number = self.request.query_params.get('page')
      number_of_items_per_page = self.request.query_params.get(
          'items')
      # Although user can request for number_of_items_per_page via the url, we set it default 40
      items_per_page = 40
      start = 0
      end = items_per_page

      if(page_number != None and number_of_items_per_page != None):
          start = int(number_of_items_per_page) * \
              int(page_number) - int(number_of_items_per_page)
          end = int(number_of_items_per_page) * int(page_number)

      elif(page_number != None and number_of_items_per_page == None):
          start = items_per_page * int(page_number) - items_per_page
          end = items_per_page * int(page_number)

      elif(page_number == None and number_of_items_per_page != None):
          # Since user didn't give page_number, we assume he wants the first page (i,e page_number = 1)
          start = int(number_of_items_per_page) * 1 - \
              int(number_of_items_per_page)
          end = int(number_of_items_per_page) * 1

      if(page_number == None):
          page_number = 1

      queryset = queryset[start:end]

      serializer = self.get_serializer(queryset, many=True)
      return Response(
          data={
              'status': True,
              'page_number': page_number,
              'total': len(serializer.data),
              'message': "All tokens",
              'data': serializer.data
          },
          status=status.HTTP_200_OK
      )

    except Exception as ex:
      return Response(
        data={
          'status': False,
          'message': "Something wrong"
        },
        status=status.HTTP_404_NOT_FOUND
      )


  def retrieve(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      #above line will create an instance with the provided 'id' in the url. Since, we
      #setup 'lookup_field=id', it will search the 'id' column with the provided id.

      serializer = self.get_serializer(instance) # serializing the queryied data
      return Response(
        data={
          'status': True,
          'message': "Tokens information",
          'data': serializer.data
        },
        status=status.HTTP_200_OK
      )

    except Exception as ex:
      return Response(
        data={
          'status': False,
          'message': "Token not found"
        },
        status=status.HTTP_404_NOT_FOUND
      )

    