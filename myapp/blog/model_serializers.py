from rest_framework.serializers import ModelSerializer
from . models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime















class contactUsSerializer(ModelSerializer):
    class Meta:
        
        
        model = contactUs
        fields = '__all__'







class oldPollsSerializer(ModelSerializer):
    
    class Meta:
        
        model = oldPolls
        fields = ('__all__')




class pollsSerializer(ModelSerializer):
    
    class Meta :
        
        model = polls
        fields = ('__all__')





class choiceSerializer(ModelSerializer):
    
    class Meta:
        model = choice
        fields  = ('__all__')





class commentReplySerializer(ModelSerializer):
    
    class Meta:
        
        model = commentReply
        fields = ('__all__')




class commentsSerializer(ModelSerializer):
    
    class Meta:
        
        model = comments
        fields = ('__all__')










class contactUsSerializer(ModelSerializer):
    
    class Meta:
        
        model = contactUs
        fields = ('__all__')







class updateUsernameSerializer(ModelSerializer):
    
    class Meta:
        
        model = updateUsername
        fields=('currentUsername','newUsername')

    
    
    
    
class updatePasswordSerializer(ModelSerializer):
    
    class Meta:
        model = updatePassword
        fields= ('currentPassword','newPassword','confirmNewPassword')
    
    


class userRegisterSerializer(ModelSerializer):
       
       class Meta:
           model = User
           fields = ('username', 'password', 'email')
  
  
  
  
  
class userLoginSerializer(ModelSerializer):
    
    class Meta:
        
        model = userLogin
        fields = ('email','password')
        






class allPostsSerializer(serializers.ModelSerializer):
    
   

    class Meta:
        model = allPosts
        fields = ('__all__')
       

        
        
        
        
        
        
        
class authorsSerializer(ModelSerializer):
    class Meta:
        model = authors
        
        fields = ('authorName','about','avatar','expertise')
        
        
        
    

        
        


class wallpapersSerializer(ModelSerializer):
    class Meta :
        model = wallpapers
        fields = ('title','slug','date','thumbnail','device','image','resolution')
        
        
        
        
        
        
        
class albumsSerializer(ModelSerializer):
   
    class Meta : 
       
        model = albums
        
        fields = ('title','date','image','totalFileSize','zipFile','slug','description','soundTracks')
        
        
        
        
        


class soundTracksSerializer(ModelSerializer):
   
   class Meta :
      
      model = soundTracks
      
      fields = ('title','artists','duration','date','image','audioFile','fileSize','album')
   
   
   
   
   
class bazi100TeamSerializer(ModelSerializer):
    
    class Meta:
        
        model = bazi100Team
        fields = ('__all__')