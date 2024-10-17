# azure/__init__.py
from .gpt35turbo import AzureGPT35Turbo as azure_gpt_35_turbo
from .gpt35turbo16k import AzureGPT35Turbo16k as azure_gpt_35_turbo_16k
from .gpt4turbo import AzureGPT4Turbo as azure_gpt_4_turbo
from .gpt4o import AzureGPT4o as azure_gpt_4o
from .gpt4omini import AzureGPT4oMini as azure_gpt_4o_mini
from .o1preview import Azureo1Preview as azure_o1_preview
from .o1mini import Azureo1Mini as azure_o1_mini
from .gpt4 import AzureGPT4 as azure_gpt_4
from .gpt432k import AzureGPT432k as azure_gpt_4_32k
from .azure import AzureOpenAI

__all__ = ['azure_gpt_35_turbo', 'azure_gpt_35_turbo_16k', 'azure_gpt_4_turbo', 'azure_gpt_4o', 'azure_4o_mini', 'azure_o1_preview', 'azure_o1_mini', 'azure_gpt_4', 'azure_gpt_4_32k']
