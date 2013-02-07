from django.conf import settings
from django.contrib.sites.models import Site
from django.http import HttpRequest
import re

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local
 
_thread_locals = local()
 
reg_b = re.compile(r"ipad|android|avantgo|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|symbian|treo|up\\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino", re.I|re.M)
reg_v = re.compile(r"1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\\-(n|u)|c55\\/|capi|ccwa|cdm\\-|cell|chtm|cldc|cmd\\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\\-s|devi|dica|dmob|do(c|p)o|ds(12|\\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\\-|_)|g1 u|g560|gene|gf\\-5|g\\-mo|go(\\.w|od)|gr(ad|un)|haie|hcit|hd\\-(m|p|t)|hei\\-|hi(pt|ta)|hp( i|ip)|hs\\-c|ht(c(\\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\\-(20|go|ma)|i230|iac( |\\-|\\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\\/)|klon|kpt |kwc\\-|kyo(c|k)|le(no|xi)|lg( g|\\/(k|l|u)|50|54|e\\-|e\\/|\\-[a-w])|libw|lynx|m1\\-w|m3ga|m50\\/|ma(te|ui|xo)|mc(01|21|ca)|m\\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\\-2|po(ck|rt|se)|prox|psio|pt\\-g|qa\\-a|qc(07|12|21|32|60|\\-[2-7]|i\\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\\-|oo|p\\-)|sdk\\/|se(c(\\-|0|1)|47|mc|nd|ri)|sgh\\-|shar|sie(\\-|m)|sk\\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\\-|v\\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\\-|tdg\\-|tel(i|m)|tim\\-|t\\-mo|to(pl|sh)|ts(70|m\\-|m3|m5)|tx\\-9|up(\\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|xda(\\-|2|g)|yas\\-|your|zeto|zte\\-", re.I|re.M)
ip_ranges = {
    157:[
        (
            100,(0,255),(0,255),
        )
    ],

    186:[
        (
            3,(0,63),(0,255),
        ),
        (
            42,(0,127),(0,255),
        ),
        (
            66,(0,127),(0,255),
        ),
        (
            66,(128,255),(0,255),
        ),
        (
            68,(0,255),(0,255),
        ),
    ],
        
    190:[
        (
            9,(160,175),(0,255),
        ),
        (
            9,(176,191),(0,255),
        ),
        (
            10,(128,191),(0,255),
        ),
        (
            10,(128,191),(0,255),
        ),
        (
            (11,12),(0,31),(0,255),
        ),
        (
            12,(32,63),(0,255),
        ),
        (
            12,(32,63),(0,255),
        ),
        (
            15,(128,143),(0,255),
        ),
        (
            52,(192,207),(0,255),
        ),
        (
            52,(64,79),(0,255),
        ),
        (
            94,(128,159),(0,255),
        ),
        (
            95,(128,159),(0,255),
        ),
        (
            95,(160,191),(0,255),
        ),
        (
            95,(192,223),(0,255),
        ),
        (
            95,(224,255),(0,255),
        ),
        (
            107,(64,79),(0,255),
        ),
        (
            120,(64,79),(0,255),
        ),
        (
            123,(0,15),(0,255),
        ),
        (
            131,(0,63),(0,255),
        ),
        (
            131,(64,127),(0,255),
        ),
        (
            152,(0,127),(0,255),
        ),
        (
            152,(128,255),(0,255),
        ),
        (
            154,(0,127),(0,255),
        ),
        (
            154,(128,255),(0,255),
        ),
        (
            155,(0,127),(0,255),
        ),
        (
            155,(128,255),(0,255),
        ),
        (
            214,(0,127),(0,255),
        ),
        (
            214,(128,255),(0,255),
        ),
        
    ],
    
    200:[
        (
            7,(192,223),(0,255),
        ),
        (
            7,(224,255),(0,255),
        ),
        (
            24,(192,223),(0,255),
        ),
        (
            25,(128,159),(0,255),
        ),
        (
            25,(160,191),(0,255),
        ),
        (
            25,(192,207),(0,255),
        ),
        (
            25,(208,223),(0,255),
        ),
        (
            55,(224,239),(0,255),
        ),
        (
            63,(192,255),(0,255),
        ),
        (
            69,(160,191),(0,255),
        ),
        (
            93,(192,239),(0,255),
        ),
        (
            105,(224,255),(0,255),
        ),
        (
            107,(0,63),(0,255),
        ),
        (
            110,(64,95),(0,255),
        ),
        (
            115,(32,47),(0,255),
        ),
        (
            115,(32,47),(0,255),
        ),
        (
            124,(224,255),(0,255),
        ),
        (
            125,(128,159),(0,255),
        ),
        (
            125,(192,255),(0,255),
        ),
        (
            126,(0,31),(0,255),
        ),
 
    ],
    
    201:[
        (
            217,(64,127),(0,255),
        ),
        (
            218,(32,63),(0,255),
        ),
        (
            219,(0,63),(0,255),
        ),
        (
            238,(160,191),(0,255),
        ),
        
        
    ]
    
}

def get_current_request():
    return getattr(_thread_locals, 'request', None)
 
class MobileMiddleware():
    
    def process_request(self, request):
        request.is_mobile = False
        if request.META.has_key('HTTP_USER_AGENT'):
            user_agent = request.META['HTTP_USER_AGENT']
            b = reg_b.search(user_agent)
            v = reg_v.search(user_agent[0:4])
            if b or v:
                #this is a mobile request
                request.is_mobile = True
                
        print("is_mobile: " + str(request.is_mobile))
        _thread_locals.request = request

class IpCheckMiddleware:
    
    def process_request(self, request):
        try:
        
            client_address = request.META['HTTP_X_FORWARDED_FOR']
            ip = client_address;
        
            request.session['isECUADOR'] = check_range(ip_ranges, ip)
        except KeyError:
            request.session['isECUADOR'] = False
        
  
    def split_ip(ip):
        """
        Returns a list comprehension of ip address octet values as integers.
        >>> split_ip('10.0.0.1')
        ... [10, 0, 0, 1]
        """
        return [int(x) for x in ip.split('.')]
        
    def check_range(ranges, ip):
        """
        Loops through an ip range dictionary determining if the given ip is contained
        within the given ranges.
        """
        in_ranges = True
        count = 1
        for r in ranges:
            if in_ranges:
                if type(r) is tuple:
                    if ip[count] in range(r[0], r[1]+1):
                        in_ranges = True
                    else:
                        in_ranges = False
                else:
                    if r == ip[count]:
                        in_ranges = True
                    else:
                        in_ranges = False
                count += 1
        return in_ranges
    
    def is_target_ip(ip):
        """
        Determines whether the given ip matches any of our defined ip ranges.
        """
        ip = split_ip(ip)
        if ip_ranges.has_key(ip[0]):
            ranges = ip_ranges[ip[0]]
            for r in ranges:
                if check_range(r, ip):
                    return True
        return False
    
    


