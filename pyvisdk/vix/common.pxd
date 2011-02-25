""" Common Definitions """

cdef extern from "stdio.h":
    ctypedef struct FILE:
        int _fileno
    enum:
        EOF = -1
    FILE *stdout
    FILE *fdopen(int fildes, char *mode)
    FILE *fopen(char *path, char *mode)
    int fclose(FILE *stream)
    int fileno(FILE *stream)

cdef extern from "errno.h":
    cdef int errno

cdef extern from "string.h":
    char *strerror(int errnum)
    char *strcpy(char *restrict, char *restrict)
    void* memset(void*,int,size_t)
    void* memcpy(void*,void*,size_t)
    char* strdup(char*)

cdef extern from "stdlib.h":
    void free(void *ptr)
    void *malloc(int)

# From the Cython FAQ, but according to a useful message on the Pyrex mailing
# list, also applicable to Pyrex
cdef extern from *:
    ctypedef void* const_void_ptr "const void*"
    ctypedef char* const_char_ptr "const char*"

# Copied from the Pyrex documentation...
cdef extern from "Python.h":
    # Return a new string object with a copy of the string v as value and
    # length len on success, and NULL on failure. If v is NULL, the contents of
    # the string are uninitialized.
    object PyString_FromStringAndSize(char *v, int len)

    # Return a NUL-terminated representation of the contents of the object obj
    # through the output variables buffer and length. 
    #
    # The function accepts both string and Unicode objects as input. For
    # Unicode objects it returns the default encoded version of the object. If
    # length is NULL, the resulting buffer may not contain NUL characters; if
    # it does, the function returns -1 and a TypeError is raised. 
    #
    # The buffer refers to an internal string buffer of obj, not a copy. The
    # data must not be modified in any way, unless the string was just created
    # using PyString_FromStringAndSize(NULL, size). It must not be deallocated.
    # If string is a Unicode object, this function computes the default
    # encoding of string and operates on that. If string is not a string object
    # at all, PyString_AsStringAndSize() returns -1 and raises TypeError.
    int PyString_AsStringAndSize(object obj, char **buffer, Py_ssize_t* length) except -1

    # Returns a pointer to a read-only memory location containing arbitrary
    # data. The obj argument must support the single-segment readable buffer
    # interface. On success, returns 0, sets buffer to the memory location and
    # buffer_len to the buffer length. Returns -1 and sets a TypeError on
    # error.
    int PyObject_AsReadBuffer(object obj, const_void_ptr *buffer, Py_ssize_t *buffer_len) except -1

    # Unfortunately, there are two common ways of implementing a va_list,
    # and we just have to guess which is being used. For the moment, though,
    # just take advantage of the fact that the following seems to work for
    # our purposes...
    ctypedef void * va_list

cdef extern from "Python.h":
    FILE *PySys_GetFile(char *name, FILE *default)

cdef extern from "stdint.h":
    ctypedef unsigned char      uint8
    ctypedef unsigned           uint16
    ctypedef unsigned long      uint32
    ctypedef unsigned long long uint64
    ctypedef   signed char      int8
    ctypedef          int       int16
    ctypedef          long      int32
    ctypedef          long long int64

ctypedef unsigned short Bool

# PIDs are too long for 16 bits, short enough to fit in 32
ctypedef uint32   PID

# ----------------------------------------------------------------------
# vim: set filetype=python expandtab shiftwidth=4:
# [X]Emacs local variables declaration - place us into python mode
# Local Variables:
# mode:python
# py-indent-offset:4
# End:
