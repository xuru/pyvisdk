
==================================================================================================
SharesLevel
==================================================================================================

.. describe:: SharesLevel

    Simplified shares notation. These designations have different meanings for different resources.
    
    
    .. py:data:: SharesLevel.custom
    
        Shares are specified in the "shares" column.
        
    
    .. py:data:: SharesLevel.high
    
        For CPU: Shares = 2000 * number of virtual CPUs For Memory: Shares = 20 * virtual machine memory size in megabytes For Disk: Shares = 2000 For Network: Shares = networkResourcePoolHighShareValue
        
    
    .. py:data:: SharesLevel.low
    
        For CPU: Shares = 500 * number of virtual CPUs For Memory: Shares = 5 * virtual machine memory size in megabytes For Disk: Shares = 500 For Network: Shares = 0.25 * networkResourcePoolHighShareValue
        
    
    .. py:data:: SharesLevel.normal
    
        For CPU: Shares = 1000 * number of virtual CPUs For Memory: Shares = 10 * virtual machine memory size in megabytes For Disk: Shares = 1000 For Network: Shares = 0.5 * networkResourcePoolHighShareValue
        
    