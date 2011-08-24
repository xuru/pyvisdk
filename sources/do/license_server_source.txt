
================================================================================
LicenseServerSource
================================================================================


.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.license_source.LicenseSource`
    
.. class:: pyvisdk.do.license_server_source.LicenseServerSource
    
    .. py:attribute:: licenseServer
    
        This property defines the server to establish a TCP session to obtain license data. Format of string is host:port Port is optional unsigned 16 bit integer license server is listening on. A trailing colon ':' without a port number is a valid expression. Host can either be an IPv4 address in dotted quad format or a resolvable DNS name <=254 characters. See RFC 3696.
        
    