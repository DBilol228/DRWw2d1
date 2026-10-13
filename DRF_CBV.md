# Class-Based Views (CBV) in Django REST Framework

## 1. Introduction

Class-Based Views (CBV) in Django REST Framework (DRF) provide a structured way to build APIs. This lecture focuses on three levels:

* APIView (low-level)
* GenericAPIView (mid-level)
* ModelViewSet (high-level)

Also includes:

* Swagger setup
* Ready-made generic classes (ListAPIView, CreateAPIView, etc.)

---

## 2. Swagger Setup (drf-yasg)

### Installation

```bash
pip install drf-yasg
```

### settings.py

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_yasg',
]
```

### urls.py (project level)

```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
```

### Optional (APIView / ViewSet annotations)

```python
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(request_body=StudentSerializer)
def post(self, request):
    ...
```

---

## 3. APIView

### What you implement

**CRUD + DETAIL manually**

### Serializer

```python
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
```

### Views

```python
class StudentListCreateAPIView(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class StudentDetailAPIView(APIView):

    def get_object(self, pk):
        return Student.objects.get(pk=pk)

    def get(self, request, pk):
        serializer = StudentSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=204)
```

### URLs

```python
urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view()),
    path('students/<int:pk>/', StudentDetailAPIView.as_view()),
]
```

### What you can add

* permissions, authentication
* manual pagination
* swagger_auto_schema for docs

---

## 4. GenericAPIView

### Base idea

Still manual methods, but with helpers.

---

## 5. Ready Generic Views (IMPORTANT)

These are built on GenericAPIView and already implement common behavior.

### ListAPIView (GET list)

```python
from rest_framework.generics import ListAPIView

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

---

### CreateAPIView (POST)

```python
from rest_framework.generics import CreateAPIView

class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

---

### ListCreateAPIView (GET + POST)

```python
from rest_framework.generics import ListCreateAPIView

class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

---

### RetrieveAPIView (GET detail)

```python
from rest_framework.generics import RetrieveAPIView

class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

---

### UpdateAPIView (PUT/PATCH)

```python
from rest_framework.generics import UpdateAPIView

class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

---

### DestroyAPIView (DELETE)

```python
from rest_framework.generics import DestroyAPIView

class StudentDeleteAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

---

### RetrieveUpdateDestroyAPIView (FULL DETAIL CRUD)

```python
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class StudentRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

---

### URLs example

```python
urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view()),
    path('students/<int:pk>/', StudentRUDAPIView.as_view()),
]
```

---

### What you can add

* pagination (global or per view)
* filtering (search, ordering)
* override methods (get_queryset, perform_create)
* swagger works automatically

---

## 6. ModelViewSet

### What you get

Full CRUD automatically.

### View

```python
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

### Router

```python
router = DefaultRouter()
router.register('students', StudentViewSet)
urlpatterns = router.urls
```

---

### Swagger with ViewSet

Works automatically. Optional customization:

```python
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema()
def list(self, request):
    return super().list(request)
```

---

### What you can add

* @action(detail=True/False)
* custom permissions per action
* filtering, pagination
* override create/list/retrieve

---

## 7. Comparison

| Feature   | APIView | Generic Views | ModelViewSet |
| --------- | ------- | ------------- | ------------ |
| CRUD Auto | No      | Partial       | Yes          |
| Detail    | Manual  | Semi-auto     | Auto         |
| Swagger   | Manual  | Auto          | Auto         |
| URLs      | Manual  | Manual        | Router       |
| Code Size | Large   | Medium        | Small        |

---

## 8. Summary

* APIView → full control, more code

* Generic Views → best balance

* ModelViewSet → fastest development

* Swagger → connect once, works everywhere

* Generic classes → reduce boilerplate significantly
