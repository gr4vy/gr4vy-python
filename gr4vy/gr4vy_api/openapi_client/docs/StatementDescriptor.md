# StatementDescriptor

The statement descriptor is the text to be shown on the buyer's statements.  The specific usage of these fields will depend on the capabilities of the underlying PSP and bank. As a typical example, 'name' and 'description' could be concatenated using '* ' as a separator, and then the resulting descriptor would be truncated to 22 characters by the issuing bank.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Reflects your doing business as (DBA) name.  Other validations:  1. Contains only Latin characters. 2. Contain at least one letter 3. Does not contain any of the special characters &#x60;&lt; &gt; \\ &#39; \&quot; *&#x60; 4. Supports:   1. Lower case: &#x60;a-z&#x60;   2. Upper case: &#x60;A-Z&#x60;   3. Numbers: &#x60;0-9&#x60;   4. Spaces: &#x60; &#x60;   5. Special characters: &#x60;. , _ - ? + /&#x60;. | [optional] 
**description** | **str, none_type** | A short description about the purchase.  Other validations: 1. Contains only Latin characters. 2. Contain at least one letter 3. Does not contain any of the special characters &#x60;&lt; &gt; \\ &#39; \&quot; *&#x60; 4. Supports:   1. Lower case: &#x60;a-z&#x60;   2. Upper case: &#x60;A-Z&#x60;   3. Numbers: &#x60;0-9&#x60;   4. Spaces: &#x60; &#x60;   5. Special characters: &#x60;. , _ - ? + /&#x60;. | [optional] 
**city** | **str, none_type** | City from which the charge originated. | [optional] 
**phone_number** | **str, none_type** | The value in the phone number field of a customer&#39;s statement. The phone number to use for this request. This expect the number in the [E164 number standard](https://www.twilio.com/docs/glossary/what-e164). | [optional] 
**url** | **str, none_type** | The value in the URL/web address field of a customer&#39;s statement. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


