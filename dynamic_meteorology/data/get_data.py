from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    'stream'    : "oper",
    'levtype'   : "pl",
    'levelist'  : "1000/to/1",
    'param'     : "129/130/131/132",
    'dataset'   : "interim",
    'step'      : "0",
    'grid'      : "0.75/0.75",
    'time'      : "00",
    'date'      : "2005-08-29/to/2005-08-29",
    'type'      : "an",
    'class'     : "ei",
    'format'    : "netcdf",
    'target'    : "test.nc"
})
