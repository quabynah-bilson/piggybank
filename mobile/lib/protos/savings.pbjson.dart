///
//  Generated code. Do not modify.
//  source: savings.proto
//
// @dart = 2.12
// ignore_for_file: annotate_overrides,camel_case_types,constant_identifier_names,deprecated_member_use_from_same_package,directives_ordering,library_prefixes,non_constant_identifier_names,prefer_final_fields,return_of_invalid_type,unnecessary_const,unnecessary_import,unnecessary_this,unused_import,unused_shown_name

import 'dart:core' as $core;
import 'dart:convert' as $convert;
import 'dart:typed_data' as $typed_data;
@$core.Deprecated('Use transactionTypeDescriptor instead')
const TransactionType$json = const {
  '1': 'TransactionType',
  '2': const [
    const {'1': 'deposit', '2': 0},
    const {'1': 'withdrawal', '2': 1},
  ],
};

/// Descriptor for `TransactionType`. Decode as a `google.protobuf.EnumDescriptorProto`.
final $typed_data.Uint8List transactionTypeDescriptor = $convert.base64Decode('Cg9UcmFuc2FjdGlvblR5cGUSCwoHZGVwb3NpdBAAEg4KCndpdGhkcmF3YWwQAQ==');
@$core.Deprecated('Use savingsListDescriptor instead')
const SavingsList$json = const {
  '1': 'SavingsList',
  '2': const [
    const {'1': 'savings', '3': 1, '4': 3, '5': 11, '6': '.savings.Savings', '10': 'savings'},
  ],
};

/// Descriptor for `SavingsList`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List savingsListDescriptor = $convert.base64Decode('CgtTYXZpbmdzTGlzdBIqCgdzYXZpbmdzGAEgAygLMhAuc2F2aW5ncy5TYXZpbmdzUgdzYXZpbmdz');
@$core.Deprecated('Use listSavingsRequestDescriptor instead')
const ListSavingsRequest$json = const {
  '1': 'ListSavingsRequest',
  '2': const [
    const {'1': 'customer_id', '3': 1, '4': 1, '5': 9, '10': 'customerId'},
    const {'1': 'piggybank_id', '3': 2, '4': 1, '5': 9, '10': 'piggybankId'},
  ],
};

/// Descriptor for `ListSavingsRequest`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List listSavingsRequestDescriptor = $convert.base64Decode('ChJMaXN0U2F2aW5nc1JlcXVlc3QSHwoLY3VzdG9tZXJfaWQYASABKAlSCmN1c3RvbWVySWQSIQoMcGlnZ3liYW5rX2lkGAIgASgJUgtwaWdneWJhbmtJZA==');
@$core.Deprecated('Use savingsDescriptor instead')
const Savings$json = const {
  '1': 'Savings',
  '2': const [
    const {'1': 'id', '3': 1, '4': 1, '5': 9, '10': 'id'},
    const {'1': 'piggybank_id', '3': 2, '4': 1, '5': 9, '10': 'piggybankId'},
    const {'1': 'amount', '3': 3, '4': 1, '5': 1, '10': 'amount'},
    const {'1': 'transaction_date', '3': 4, '4': 1, '5': 11, '6': '.google.protobuf.Timestamp', '10': 'transactionDate'},
    const {'1': 'transaction_type', '3': 5, '4': 1, '5': 14, '6': '.savings.TransactionType', '10': 'transactionType'},
  ],
};

/// Descriptor for `Savings`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List savingsDescriptor = $convert.base64Decode('CgdTYXZpbmdzEg4KAmlkGAEgASgJUgJpZBIhCgxwaWdneWJhbmtfaWQYAiABKAlSC3BpZ2d5YmFua0lkEhYKBmFtb3VudBgDIAEoAVIGYW1vdW50EkUKEHRyYW5zYWN0aW9uX2RhdGUYBCABKAsyGi5nb29nbGUucHJvdG9idWYuVGltZXN0YW1wUg90cmFuc2FjdGlvbkRhdGUSQwoQdHJhbnNhY3Rpb25fdHlwZRgFIAEoDjIYLnNhdmluZ3MuVHJhbnNhY3Rpb25UeXBlUg90cmFuc2FjdGlvblR5cGU=');