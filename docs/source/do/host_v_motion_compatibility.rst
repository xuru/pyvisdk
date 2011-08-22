
================================================================================
HostVMotionCompatibility
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_v_motion_compatibility.QueryVMotionCompatibility`
    
.. class:: pyvisdk.do.host_v_motion_compatibility.HostVMotionCompatibility
    
    .. py:attribute:: compatibility
    
        Ways in which the host is compatible with the designated virtual machine that is a candidate for VMotion. This array will be a subset of the set of VMotionCompatibilityType strings that were input to queryVMotionCompatibility.
        
    
    .. py:attribute:: host
    
        The prospective host for the virtual machine.
        
    