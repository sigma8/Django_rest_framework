from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# Necesitamos serializar la data del snippet para poder compartirla o almacenarla
# de manera que podamos recuperar su estado o forma original


# Aqui se define que se va a serializar y deserializar
# Los indicadores de campo también pueden controlar 
# cómo se debe mostrar el serializador en determinadas circunstancias, 
# como cuando se representa en HTML. 
# El indicador {'base_template': 'textarea.html'} es equivalente a usar 
# widget=widgets. Textarea en una clase de formulario de Django.
'''
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
'''
# Usando ModelSerializers es un atajo para crear las clases serializadoras 
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
    def create(self, validated_data):
        # Crear y retornar una nueva instancia Snippet, dada una data valida

        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Actualizar y retornar un instancia Snippet existente, dada una data valida

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance