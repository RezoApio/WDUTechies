# Authentication info
```shell
dspmqaut -m IMPLL43  -t qmgr -p iiipdvo0

dspmqaut -m CMPLA19 -n CBB.GBL.ACREATE_GBO_CLAIM -t q -p ccbbmap4
Entity ccbbmap4 has the following authorizations for object CBB.GBL.ACREATE_GBO_CLAIM:
        get
        browse
        put
        inq
        dsp

setmqaut -m CMPLA19 -t q -n CBB.GBL.ACREATE_GBO_CLAIM -p ccbbmap0 +all
```

# List Msg Flows for Execution Group

```shell
mqsilist -a BMIAA0Q -e MPW_EU
BIP8131I: MessageFlow: WMB_MPW_ACKNOWLEDGEMENT_SUB00_001
BIP8131I: MessageFlow: WMB_MPW_UPDATECLAIM_SUB00_001
BIP8131I: MessageFlow: MPW_WMB_CREATECLAIM_PUB00_001

```

# List subscriptions 

## MB6

```shell
mqsibrowse BMIAA0Q -tbsubscriptions
```
## IIB 10

```shell
echo "display pubsub ALL" | runmqsc DMPLL35
```

# New Item

```shell


```

# New Item

```shell


```