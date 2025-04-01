CREATE TABLE  qc_rule_counts_history (
    batch_id        VARCHAR,
    vendor_name     VARCHAR,
    qc_rule_no      VARCHAR,
    qc_rule         VARCHAR,
    count           INTEGER,
    process_time    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
