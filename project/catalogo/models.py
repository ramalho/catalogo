from django.db import models

def create_model(name, attrs={}, meta_attrs={}, module_path='django.db.models'):
    attrs['__module__'] = module_path
    class Meta: pass
    Meta.__dict__.update(meta_attrs, __module__=module_path)
    attrs['Meta'] = Meta
    return type(name, (models.Model,), attrs)
    
Experimento = create_model('Experimento', {'nome':models.CharField(max_length=256)})
