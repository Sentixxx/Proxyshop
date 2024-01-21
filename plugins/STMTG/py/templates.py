"""
* STMTG Templates
"""
# Standard Library Imports
from functools import cached_property
from typing import Optional

# Third Party Imports
from photoshop.api._artlayer import ArtLayer

# Local Imports
from src.enums.layers import LAYERS
import src.helpers as psd
from src.templates import FullartMod

"""
* Template Classes
"""


class STDnD(FullartMod):
    
    template_suffix = "dnd"
    
    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        if self.background == LAYERS.COLORLESS:
            return
        return super().background_layer
    
    def enable_crown(self) -> None:
        super().enable_crown()
        if self.background_layer:
            psd.enable_mask(self.background_layer.parent)