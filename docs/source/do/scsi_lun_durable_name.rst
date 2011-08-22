
================================================================================
ScsiLunDurableName
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.scsi_lun.ScsiLun`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.scsi_lun_durable_name.ScsiLunDurableName
    
    .. py:attribute:: data
    
        The variable length byte array containing the namespace-specific data. For a SCSI-3 compliant device this field is the descriptor header along with the payload for data obtained from page 83h, and is the payload for data obtained from page 80h of the Vital Product Data (VPD).
        
    
    .. py:attribute:: namespace
    
        The string describing the namespace used for the durable name.
        
    
    .. py:attribute:: namespaceId
    
        The byte used by the ESX Server product to represent the namespace.
        
    