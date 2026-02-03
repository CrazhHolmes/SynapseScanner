@echo off
:: ------------------------------------------------------------
:: synapse.bat - wrapper for SynapseScanner CLI
:: Preserves quoting so multi-word queries work correctly.
:: ------------------------------------------------------------
python -m synapsescanner.universal_scanner %*
