#pragma once
const long MIN_FEE_CENTS = 50;
inline double rate_for(long amount_cents) {
    if (amount_cents <= 10000) return 0.02;
    if (amount_cents <= 100000) return 0.01;
    return 0.005;
}
inline long fee_for(long amount_cents) {
    return (long)(amount_cents * rate_for(amount_cents));
}
