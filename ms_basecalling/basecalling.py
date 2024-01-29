import logging
import math
from typing import List, Tuple, Dict

class Basecalling:
    def __init__(self,error=1E-6, printN=False):
        self.base_dict: Dict[str, float] = {
            'A': 329.0525,
            'C': 305.0413,
            'G': 345.0474,
            'U': 306.0253
        }
        self.logger = logging.getLogger(__name__)
        self.error = error
        self.printN = printN

    def identify_basecallings(self, data: List[float]) -> List[Tuple[float, float, str]]:
        """
        Function to identify basecallings in the data.
        Args:
            data: List of floats.
        Returns:
            basecallings: List of tuples, each containing two floats and a base.
        """
        basecallings = []
        for value in data:
            found_match = False
            for base, ref_value in self.base_dict.items():
                self.logger.debug(f"Comparing value with {base} and {value}")      
                if math.isclose(value, ref_value, rel_tol=self.error):
                    basecallings.append((value, base))
                    found_match = True
                    break
            if self.printN and not found_match:
                self.logger.debug(f"No match found for {value}, print N")
                basecallings.append((value, 'N'))
                
        return basecallings
