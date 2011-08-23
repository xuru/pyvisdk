
================================================================================
VirtualSIOControllerOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.int_option.IntOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_controller_option.VirtualControllerOption`
    
.. class:: pyvisdk.do.virtual_sio_controller_option.VirtualSIOControllerOption
    
    .. py:attribute:: numFloppyDrives
    
        Three properties (numFloppyDrives.min, numFloppyDrives.max, and numFloppyDrives.defaultValue) define the minimum, maximum, and default number of floppy drives you can have at any given time in the Super IO Controller. This is further constrained by the number of available slots in the Super IO Controller.
        
    
    .. py:attribute:: numParallelPorts
    
        Three properties (numParallelPorts.min, numParallelPorts.max, and numParallelPorts.defaultValue) define the minimum, maximum, and default number of parallel ports you can have at any given time in the Super IO controller. This is further constrained by the number of available slots in the Super IO Controller.
        
    
    .. py:attribute:: numSerialPorts
    
        Three properties (numSerialPorts.min, numSerialPorts.max, and numSerialPorts.defaultValue) define the minimum, maximum, and default number of serial ports you can have at any given time in the Super IO Controller. This is further constrained by the number of available slots in the Super IO Controller.
        
    