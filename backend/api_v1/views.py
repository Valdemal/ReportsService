import trml2pdf
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from drf_pdf.renderer import PDFRenderer
from drf_pdf.response import PDFResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v1.models import Report
from api_v1.serializers import ReportSerializer, ReportPrintSerializer


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    permission_classes = IsAuthenticated,
    serializer_class = ReportSerializer

    def get_renderers(self):
        if self.action == 'print':
            return PDFRenderer(), JSONRenderer()

        return JSONRenderer(),

    @extend_schema(
        request=ReportPrintSerializer,

    )
    @action(methods=['POST'], detail=True)
    def print(self, request: Request, pk: int):
        try:
            report = Report.objects.get(pk=pk)
            pdf: bytes = trml2pdf.parseString(report.template)

            return PDFResponse(pdf=pdf, file_name=report.name)
        except ObjectDoesNotExist:
            return Response(data={'detail': 'Отчет не найден'}, status=status.HTTP_404_NOT_FOUND)
