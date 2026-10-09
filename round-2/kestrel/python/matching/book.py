from __future__ import annotations

from typing import List

from .models import Resting, Trade


class OrderBook:
    def __init__(self) -> None:
        self._asks: List[Resting] = []
        self._bids: List[Resting] = []
        self._seq = 0

    def _next_seq(self) -> int:
        self._seq += 1
        return self._seq

    def cancel(self, order_id: str) -> None:
        pass

    def limit(self, order_id: str, side: str, price: int, qty: int) -> List[Trade]:
        trades: List[Trade] = []
        if side == "buy":
            book = self._asks
            book.sort(key=lambda r: (r.price, -r.seq))
            i = 0
            while qty > 0 and i < len(book):
                r = book[i]
                if r.price <= price:
                    fill = min(qty, r.qty)
                    trades.append(Trade(r.order_id, order_id, r.price, fill))
                    qty -= fill
                    book.pop(i)
                else:
                    break
            if qty > 0:
                self._bids.append(Resting(order_id, "buy", price, qty, self._next_seq()))
        else:
            book = self._bids
            book.sort(key=lambda r: (-r.price, -r.seq))
            i = 0
            while qty > 0 and i < len(book):
                r = book[i]
                if r.price >= price:
                    fill = min(qty, r.qty)
                    trades.append(Trade(r.order_id, order_id, r.price, fill))
                    qty -= fill
                    book.pop(i)
                else:
                    break
            if qty > 0:
                self._asks.append(Resting(order_id, "sell", price, qty, self._next_seq()))
        return trades
