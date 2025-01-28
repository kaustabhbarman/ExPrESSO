# ExPrESSO

## Zokrates Setup
Install Zokrates from Terminal: `curl -LSfs get.zokrat.es | sh` or build from source from [here](https://zokrates.github.io/gettingstarted.html). Also, 
get an overview of the Zokrates language syntax. 

## As a Verifier
As a verifier, you need to write a circuit and compile it to create R1 Constraint System. 
### Step 1: Prepare circuit public input
Open `input_helper.py` and replace the value of `input_string` in line `32` to the string of which the prover should prove knowledge of.
Run the python script: `input_helper.py`. The script will return two arrays. verifier, we need the second array from above which is the output of the `string_to_int_hash()` function in the python script:
In Socrates we can only hold 128-bit values, and so our 256-bit hash is split into two parts. In this case the first element for the lower 128 bits, and second element for the upper 128 bits.

### Step 2: Enter public input
Open the Circuit in `verifier.zok` using a text editor or an IDE. Change the value of `field[2] expected_hash = [x,y];` in line `7`.

### Step 3: Compile circuit
Run `zokrates compile -i verifier.zok`. This will output three files along with R1CS file.

### Step 4: Setup the Circuit
Run `zokrates setup` which will create a `verification.key` and a `proving.key`. The `proving.key` is sent to a prover who computes a proof specifically for our generated circuit.

### Step 5 (optional): Export Smart Contract
If you would like to verify a proof on-chain, then you can export a smart-contract by running: `zokrates export verifier`

This will output a deployable Solidity smart-contract named `verifier.sol` 

## As a Prover
As a prover we need to create generate a proof that a verifier can verify to know about our knowledge of a string. 

### Step 1: Prepare private input (secret)
We as a prover need to split the input into four 128-bit values, and which gives us a data input of up to 1024 bits. The values of the input will be a, b, c and d, and where d is the end part of the data buffer.

Run the python script again. The first output array with four elements is our secret input.

### Step 2: Compute Witness
Run `zokrates compute-witness -a a b c d` and replace the values `a b c d` with the four elements from Step 1 output. The computed witness `out.wtns` and `witness` file should be kept secret and not shared with anyone. 

### Step 3: Generate the proof
Run `zokrates generate-proof` to generate the proof `proof.json` which can be sent to a verifier.

### Step 4: Verification
Run `zokrates verify` to see if the proof can be verified.

If the verifier wants to verify the proof on-chain, we have to input the contents of `proof.json` in the smart contract:

The values of `proof` array is the `proof` input in the smart contract. The values of `input` goes into `input` field of the smart-contract.



