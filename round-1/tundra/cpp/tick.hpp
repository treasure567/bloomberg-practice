#pragma once
inline long round_to_tick(long price_cents, long tick_cents) {
    return (price_cents / tick_cents) * tick_cents;
}
