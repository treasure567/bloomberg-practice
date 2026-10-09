# RISK-51: Sells increase the net position

## Report

Risk numbers are wrong: a sell adds to the net position instead of reducing it. Positions are
being accumulated with the magnitude of each trade, ignoring its sign.

## Acceptance criteria

- a buy of +10 then a sell of -4 nets to 6;
- the net can be negative when sells exceed buys;
- the sign of each trade is respected as given;
- add a test that mixes a buy and a sell and asserts the signed net.

Do not change counterparty isolation as part of this ticket.
