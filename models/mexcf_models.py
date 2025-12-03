from decimal import Decimal
from pydantic import BaseModel, Field
from typing import List, Optional


class ContractInfo(BaseModel):
    symbol: str
    display_name: str = Field(alias='displayName')
    display_name_en: str = Field(alias='displayNameEn')
    position_open_type: int = Field(alias='positionOpenType')
    base_coin: str = Field(alias='baseCoin')
    quote_coin: str = Field(alias='quoteCoin')
    settle_coin: str = Field(alias='settleCoin')
    contract_size: Decimal = Field(alias='contractSize')
    min_leverage: int = Field(alias='minLeverage')
    max_leverage: int = Field(alias='maxLeverage')
    price_scale: int = Field(alias='priceScale')
    vol_scale: int = Field(alias='volScale')
    amount_scale: int = Field(alias='amountScale')
    price_unit: Decimal = Field(alias='priceUnit')
    vol_unit: int = Field(alias='volUnit')
    min_vol: Decimal = Field(alias='minVol')
    max_vol: Decimal = Field(alias='maxVol')
    bid_limit_price_rate: Decimal = Field(alias='bidLimitPriceRate')
    ask_limit_price_rate: Decimal = Field(alias='askLimitPriceRate')
    taker_fee_rate: Decimal = Field(alias='takerFeeRate')
    maker_fee_rate: Decimal = Field(alias='makerFeeRate')
    maintenance_margin_rate: Decimal = Field(alias='maintenanceMarginRate')
    initial_margin_rate: Decimal = Field(alias='initialMarginRate')
    risk_base_vol: Decimal = Field(alias='riskBaseVol')
    risk_incr_vol: Decimal = Field(alias='riskIncrVol')
    risk_long_short_switch: int = Field(alias='riskLongShortSwitch')
    risk_base_vol_long: Optional[Decimal] = Field(alias='riskBaseVolLong', default=None)
    risk_incr_vol_long: Optional[Decimal] = Field(alias='riskIncrVolLong', default=None)
    risk_base_vol_short: Optional[Decimal] = Field(alias='riskBaseVolShort', default=None)
    risk_incr_vol_short: Optional[Decimal] = Field(alias='riskIncrVolShort', default=None)
    risk_incr_mmr: Optional[Decimal] = Field(alias='riskIncrMR', default=None)
    risk_incr_imr: Optional[Decimal] = Field(alias='riskIncrImr', default=None)
    risk_level_limit: int = Field(alias='riskLevelLimit')
    price_coefficient_variation: Decimal = Field(alias='priceCoefficientVariation')
    index_origin: List[str] = Field(alias='indexOrigin', default=None)
    state: int
    api_allowed: bool = Field(alias='apiAllowed')
    concept_plate: List[str] = Field(alias='conceptPlate')
    risk_limit_type: str = Field(alias='riskLimitType')
    max_num_orders: List[int] = Field(alias='maxNumOrders')
    type: int

class RespGetContractInfo(BaseModel):
    success: bool
    code: int
    data: List[ContractInfo]
