this["JST"] = this["JST"] || {};
this["JST"]["example"] = function(obj){
var __t,__p='',__j=Array.prototype.join,print=function(){__p+=__j.call(arguments,'');};
with(obj||{}){
__p+='';
 for(var ix=0; ix < count; ix++){ 
__p+='\n  <p>'+
((__t=( name ))==null?'':_.escape(__t))+
' smells like toast!</p>\n';
 } 
__p+='\n\n';
}
return __p;
};