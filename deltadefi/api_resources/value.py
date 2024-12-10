from typing import Dict, List, Tuple

class Asset: # TODO: import Asset
    unit: str
    quantity: int

class Value:
    value: Dict[str, int]

    def __init__(self) -> None:
        self.value = {}

    """
    * Add an asset to the Value class's value record. If an asset with the same unit already exists in the value record, the quantity of the
    * existing asset will be increased by the quantity of the new asset. If no such asset exists, the new asset will be added to the value record.
    * Implementation:
    * 1. Check if the unit of the asset already exists in the value record.
    * 2. If the unit exists, add the new quantity to the existing quantity.
    * 3. If the unit does not exist, add the unti to the object.
    * 4. Return the Value class instance.
    * @param asset
    * @returns this
    """
    def add_asset(self, asset: Asset) -> 'Value':
        quantity = asset.quantity
        unit = asset.unit

        if unit in self.value:
            self.value[unit] += quantity
        else:
            self.value[unit] = quantity
        return self
    
    """
     * Add an array of assets to the Value class's value record. If an asset with the same unit already exists in the value record, the quantity of the
     * existing asset will be increased by the quantity of the new asset. If no such asset exists, the new assets under the array of assets will be added to the value record.
     * Implementation:
     * 1. Iterate over each asset in the 'assets' array.
     * 2. For each asset, check if the unit of the asset already exists in the value record.
     * 3. If the unit exists, add the new quantity to the existing quantity.
     * 4. If the unit does not exist, add the unti to the object.
     * 5. Return the Value class instance.
     * @param assets
     * @returns this
    """
    def add_assets(self, assets: List[Asset]) -> 'Value':
        for asset in assets:
            self.add_asset(asset)
        return self

    """
     * Substract an asset from the Value class's value record. If an asset with the same unit already exists in the value record, the quantity of the
     * existing asset will be decreased by the quantity of the new asset. If no such asset exists, an error message should be printed.
     * Implementation:
     * 1. Check if the unit of the asset already exists in the value record.
     * 2. If the unit exists, subtract the new quantity from the existing quantity.
     * 3. If the unit does not exist, print an error message.
     * @param asset
     * @returns this
    """
    def negate_asset(self, asset: Asset) -> 'Value':
        unit = asset.unit
        quantity = asset.quantity

        current_quantity = self.value.get(unit, 0)
        new_quantity = current_quantity - quantity

        if new_quantity == 0:
            del self.value[unit]
        else:
            self.value[unit] = new_quantity
        return self

    """
     * Subtract an array of assets from the Value class's value record. If an asset with the same unit already exists in the value record, the quantity of the
     * existing asset will be decreased by the quantity of the new asset. If no such asset exists, an error message should be printed.
     * @param assets
     * @returns this
    """
    def negate_assets(self, assets: List[Asset]) -> 'Value':
        for asset in assets:
            self.negate_asset(asset)
        return self

    # """
    #  * Get the quantity of asset object per unit
    #  * @param unit
    #  * @returns
    # """
    # def get(self, unit: str) -> int:
    #     return self.value.get(unit, 0)

    """
     * Get all assets (return Record of Asset[])
     * @param
     * @returns Record<string, Asset[]>
    """
    def units(self) -> Dict[str, List[Tuple[str, int]]]:
        result = {}
        for unit, quantity in self.value.items():
            if unit not in result:
                result[unit] = []
            result[unit].append((unit, quantity))
        return result

    """
     * Check if the value is greater than or equal to an inputted value
     * @param unit - The unit to compare (e.g., "ADA")
     * @param other - The value to compare against
     * @returns boolean
    """
    def geq(self, unit: str, other: 'Value') -> bool:
        if unit not in self.value or unit not in other.value:
            return False
        return self.value[unit] >= other.value[unit]

    """
     * Check if the value is less than or equal to an inputted value
     * @param unit - The unit to compare (e.g., "ADA")
     * @param other - The value to compare against
     * @returns boolean
    """
    def leq(self, unit: str, other: 'Value') -> bool:
        if unit not in self.value or unit not in other.value:
            return False
        return self.value[unit] <= other.value[unit]

    """
     * Check if the value is empty
     * @param
     * @returns boolean
    """
    def is_empty(self) -> bool:
        return not self.value

    """
     * Merge the given values
     * @param values
     * @returns this
    """
    def merge(self, values: 'Value' | List['Value']) -> 'Value':
        if isinstance(values, list):
            values_list = values
        else:
            values_list = [values]

        for other in values_list:
            for unit, quantity in other.value.items():
                self.value[unit] = self.value.get(unit, 0) + quantity

        return self