from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import  permission_classes

from .models import ToDo
from .serializer import ToDoSerializer
from .permissions import IsOwner


#--------------------------------API FOR TO DO DATA -----------------------------#   

@permission_classes([permissions.IsAuthenticated])
class GetTodoListAPIView(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all().order_by('-timestamp')
    permissions = (permissions.IsAuthenticated, IsOwner, )
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
        

#--------------------------------API FOR TO DO DATA -----------------------------#  

# @permission_classes([permissions.IsAuthenticated])
# class PostTodoAPIView(generics.GenericAPIView):
#     serializer_class = ToDoSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data = request.data)
#         if serializer.is_valid():
#             serializer.save(user = request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         else:
#             return Response({'message': 'Have some field is not valid!'}, status=status.HTTP_400_BAD_REQUEST)


#-------------------------------------------------------------#

@permission_classes([permissions.IsAuthenticated])
class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all().order_by('-timestamp')
    permissions = (permissions.IsAuthenticated, IsOwner, )
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

