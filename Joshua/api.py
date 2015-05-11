from tastypie import fields
from tastypie.bundle import Bundle

import subprocess
from Joshua.cors import CORSModelResource
from Joshua.settings import JOSHUA_SCRIPT_EXECUTABLE
from Joshua.settings import JOSHUA_SCRIPT_FILENAME
import json


class TranslationResource(CORSModelResource):
    orig_language = fields.CharField( help_text="Original language, ISO 2 letter language code. For example ar ")
    orig_text = fields.CharField(help_text="Unicode String data in encoded UTF8 format")    
    translated_text = fields.CharField(help_text="translated text in English")
   
    class Meta:      
        resource_name = 'translation'
        #always return data even for post
        always_return_data =True
        allowed_methods = ['get', 'post']
        include_resource_uri=False
        collection_name = 'translations'

      

    # The following methods will need overriding regardless of your
    # data source.
    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.request.GET.get('orig_text', "")
        else:
            kwargs['pk'] = bundle_or_obj.GET.get('orig_text', "")
        
        return kwargs
    
   
    def obj_get(self, bundle, **kwargs):
        
        return {}
    
    #handle post request
    def obj_create(self, bundle, **kwargs):
       
        return bundle
    
    def get_object_list(self, request):
    #go ahread return empty result. dehydrate method will take care of final output
        results = []   
        new_dict = {}
                
        results.append(new_dict)

        return results

    def obj_get_list(self, bundle, **kwargs):
        # Filtering disabled for brevity...
        return self.get_object_list(bundle.request)
    def  get_value_by_key(self, bundle, key):
        if(bundle.request.method=="GET" and  key in bundle.request.GET):
            return bundle.request.GET[key]
        elif(bundle.request.method=="POST"):
            
            d = json.loads(bundle.request.body.decode("utf-8"))  # @UndefinedVariable
            return d.get(key, "")
            
        else:
            return ""
        
    
    def translate(self, bundle):
        translated = ""
        orig_lang_key="orig_language"
        org_text_key="orig_text"
        if (self.get_value_by_key(bundle, orig_lang_key) != "" and self.get_value_by_key(bundle, org_text_key)!=""):
            #stdin includes orig_language space and orig_text
            txt=  (self.get_value_by_key(bundle, orig_lang_key)+" "+self.get_value_by_key(bundle, org_text_key)).encode('utf-8')
        
            pipe = subprocess.Popen([JOSHUA_SCRIPT_EXECUTABLE, JOSHUA_SCRIPT_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            command_stdout=pipe.communicate(txt)[0]
                
            try:
                translated=command_stdout.decode(encoding='utf8')
            except Exception as e:
                    print("calling "+JOSHUA_SCRIPT_EXECUTABLE+" "+ JOSHUA_SCRIPT_FILENAME+ "failed. error: "+e)
                 
        
        return translated;
    
    def dehydrate(self, bundle):
        orig_lang_key="orig_language"
        org_text_key="orig_text"
        bundle.data[orig_lang_key]=self.get_value_by_key(bundle, orig_lang_key)
        bundle.data[org_text_key]=self.get_value_by_key(bundle, org_text_key)
        
        bundle.data['translated_text']=self.translate(bundle)
        return bundle;
    
