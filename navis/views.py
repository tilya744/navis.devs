from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import SendCreateFeedbackSerializer
from .models import *
from asyncio import run
from tg_bot.bot import send_feedback


class SendCreateFeedbackAPIVIew(generics.CreateAPIView):
    serializer_class = SendCreateFeedbackSerializer
    queryset = Feedback.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            msg = run(send_feedback(serializer.data))
            if msg:
                return Response({'response': True}, status=status.HTTP_200_OK)
            return Response({'response': False})
        return Response({'response': False, 'error': serializer.errors})

