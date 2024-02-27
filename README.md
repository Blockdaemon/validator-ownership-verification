
## Verifying proof of validator ownership
Example validator: https://holesky.beaconcha.in/validator/a9ff82d286231f065170aa795777896152d79f81e40279f62bb7e9a354f86f227c1b93582ac42e2b1340326ad08ea141

1. Obtain validator private key from validator client. See Prysm example:
```shell
/validator --config-file=/config/validator-config.yaml accounts list --show-private-keys
```

2. Owner signs aribitrary message with validator private key
```shell
$ pip install -r requirements.txt 
$ python bls-sign-msg.py $PRIVATEKEY "hello world"
:: public key from private key: a9ff82d286231f065170aa795777896152d79f81e40279f62bb7e9a354f86f227c1b93582ac42e2b1340326ad08ea141
:: message signature: 95f7af6f246dae0ec150cfcd51699c4bea51b9048dfe07cf6c177b4cfa705554c5a3c4282485c5d5f23f6d2827e2fffa0203e5f6e99081824ea651c288ad3c88d1a48f8340a28fb12a3341591c9d49a64abb495297eb06245fa5f4b9d81ffbdf
```

3. Verify signature with validator public key, signature and message
```shell
$ python bls-verify-signature.py a9ff82d286231f065170aa795777896152d79f81e40279f62bb7e9a354f86f227c1b93582ac42e2b1340326ad08ea141 95f7af6f246dae0ec150cfcd51699c4bea51b9048dfe07cf6c177b4cfa705554c5a3c4282485c5d5f23f6d2827e2fffa0203e5f6e99081824ea651c288ad3c88d1a48f8340a28fb12a3341591c9d49a64abb495297eb06245fa5f4b9d81ffbdf "hello world"
:: verified signature: True
```
