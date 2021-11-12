from typing import List, Optional, Any
from datetime import datetime


class Persons:
    first_name: str
    middle_name: str
    last_name: str
    full_name: str
    phone_number: str

    def __init__(self, first_name: str, middle_name: str, last_name: str, full_name: str, phone_number: str) -> None:
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.full_name = full_name
        self.phone_number = phone_number


class AttorneyAgentInformationDatum:
    persons: Persons
    registration_number: int

    def __init__(self, persons: Persons, registration_number: int) -> None:
        self.persons = persons
        self.registration_number = registration_number


class AddressElement:
    address_line1: str
    address_line2: str
    city_name: str
    geographic_region_code: str
    postal_code: str

    def __init__(self, address_line1: str, address_line2: str, city_name: str, geographic_region_code: str, postal_code: str) -> None:
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city_name = city_name
        self.geographic_region_code = geographic_region_code
        self.postal_code = postal_code


class CorrespondenceAddressDatum:
    customer_number: int
    name: str
    address: List[AddressElement]

    def __init__(self, customer_number: int, name: str, address: List[AddressElement]) -> None:
        self.customer_number = customer_number
        self.name = name
        self.address = address


class AttorneyInformationDataBag:
    mx_source: str
    mx_synced_date: str
    correspondence_address_data: List[CorrespondenceAddressDatum]
    attorney_agent_information_data: List[AttorneyAgentInformationDatum]

    def __init__(self, mx_source: str, mx_synced_date: str, correspondence_address_data: List[CorrespondenceAddressDatum], attorney_agent_information_data: List[AttorneyAgentInformationDatum]) -> None:
        self.mx_source = mx_source
        self.mx_synced_date = mx_synced_date
        self.correspondence_address_data = correspondence_address_data
        self.attorney_agent_information_data = attorney_agent_information_data


class ContinuityDatum:
    application_number: str
    description: str
    filing_date: datetime
    continuity_status: str
    patent_number: str
    aia: Optional[str]

    


class ContinuityDataBag:
    mx_source: str
    mx_synced_date: str
    parent_continuity_data: List[ContinuityDatum]
    child_continuity_data: List[ContinuityDatum]

    def __init__(self, mx_source: str, mx_synced_date: str, parent_continuity_data: List[ContinuityDatum], child_continuity_data: List[ContinuityDatum]) -> None:
        self.mx_source = mx_source
        self.mx_synced_date = mx_synced_date
        self.parent_continuity_data = parent_continuity_data
        self.child_continuity_data = child_continuity_data


class ForeignPriorityDatum:
    country: str
    priority: str
    priority_date: datetime

    def __init__(self, country: str, priority: str, priority_date: datetime) -> None:
        self.country = country
        self.priority = priority
        self.priority_date = priority_date


class ForeignPriorityDataBag:
    mx_source: str
    mx_synced_date: str
    foreign_priority_data: List[ForeignPriorityDatum]

    def __init__(self, mx_source: str, mx_synced_date: str, foreign_priority_data: List[ForeignPriorityDatum]) -> None:
        self.mx_source = mx_source
        self.mx_synced_date = mx_synced_date
        self.foreign_priority_data = foreign_priority_data


class ApplicationReference:
    country_code: str
    document_number: str
    kind_code: Optional[str]
    filing_date: datetime
    format: str

    def __init__(self, country_code: str, document_number: str, kind_code: Optional[str], filing_date: datetime, format: str) -> None:
        self.country_code = country_code
        self.document_number = document_number
        self.kind_code = kind_code
        self.filing_date = filing_date
        self.format = format


class Claims:
    total_claims: str
    independent_claims: str
    claim_text: None

    def __init__(self, total_claims: str, independent_claims: str, claim_text: None) -> None:
        self.total_claims = total_claims
        self.independent_claims = independent_claims
        self.claim_text = claim_text


class NationalClassification:
    national_class: None
    national_sub_class: None

    def __init__(self, national_class: None, national_sub_class: None) -> None:
        self.national_class = national_class
        self.national_sub_class = national_sub_class


class ApplicantAddress:
    street: None
    city: Optional[str]
    country: str
    state: Optional[str]

    def __init__(self, street: None, city: Optional[str], country: str, state: Optional[str]) -> None:
        self.street = street
        self.city = city
        self.country = country
        self.state = state


class Applicant:
    full_name: str
    first_name: Optional[str]
    last_name: Optional[str]
    address: ApplicantAddress


class Parties:
    applicants: List[Applicant]
    agents: None
    examiners: None
    inventors: List[Applicant]
    assignees: None
    assignee_history: None
    mx_first_named_applicant: str
    mx_first_named_inventor: str


class PatentGrantIdentification:
    grant_date: None
    patent_number: None

    def __init__(self, grant_date: None, patent_number: None) -> None:
        self.grant_date = grant_date
        self.patent_number = patent_number


class PatentPublicationIdentification:
    publication_date: None
    publication_number: None


class ExpirationDate:
    anticipated_date: None
    adjusted_date: None

    def __init__(self, anticipated_date: None, adjusted_date: None) -> None:
        self.anticipated_date = anticipated_date
        self.adjusted_date = adjusted_date


class PatentStatus:
    status_description: str
    term_extension: str
    term_disclosure: bool
    expiration_date: ExpirationDate


class PriorityClaims:
    priority_claim: None

    def __init__(self, priority_claim: None) -> None:
        self.priority_claim = priority_claim


class TechnicalData:
    classifications_ipcr: None
    classifications_cpc: None
    invention_title: str
    citation: None


class PatentCaseMetaData:
    mx_status: bool
    mx_error: List[Any]
    mx_synced_date: datetime
    mx_source: str
    application_reference: List[ApplicationReference]
    patent_grant_identification: PatentGrantIdentification
    patent_publication_identification: PatentPublicationIdentification
    case_type: str
    filing_date: datetime
    application_type_category: str
    country_code: str
    national_classification: NationalClassification
    applicant_file_reference: None
    business_entity_status_category: str
    mx_pto_link: None
    technical_data: TechnicalData
    registration_date: None
    group_art_unit: str
    patent_status: PatentStatus
    parties: Parties
    description: str
    priority_claims: PriorityClaims
    claims: Claims
    abstract: str
    family: None



class PatentTermAdjustmentHistoryDatum:
    event_sequence_number: int
    event_date: datetime
    event_description_text: str
    ip_office_day_delay_quantity: int
    applicant_day_delay_quantity: int
    originating_event_sequence_number: int

    def __init__(self, event_sequence_number: int, event_date: datetime, event_description_text: str, ip_office_day_delay_quantity: int, applicant_day_delay_quantity: int, originating_event_sequence_number: int) -> None:
        self.event_sequence_number = event_sequence_number
        self.event_date = event_date
        self.event_description_text = event_description_text
        self.ip_office_day_delay_quantity = ip_office_day_delay_quantity
        self.applicant_day_delay_quantity = applicant_day_delay_quantity
        self.originating_event_sequence_number = originating_event_sequence_number


class PatentTermAdjustmentHistoryDataBag:
    patent_term_adjustment_history_data: List[PatentTermAdjustmentHistoryDatum]

    def __init__(self, patent_term_adjustment_history_data: List[PatentTermAdjustmentHistoryDatum]) -> None:
        self.patent_term_adjustment_history_data = patent_term_adjustment_history_data


class PatentTermAdjustmentData:
    a_delay_quantity: int
    b_delay_quantity: int
    c_delay_quantity: int
    overlapping_day_quantity: int
    non_overlapping_day_quantity: int
    ip_office_day_delay_quantity: int
    applicant_day_delay_quantity: int
    adjustment_total_quantity: int
    patent_term_adjustment_history_data_bag: PatentTermAdjustmentHistoryDataBag

    def __init__(self, a_delay_quantity: int, b_delay_quantity: int, c_delay_quantity: int, overlapping_day_quantity: int, non_overlapping_day_quantity: int, ip_office_day_delay_quantity: int, applicant_day_delay_quantity: int, adjustment_total_quantity: int, patent_term_adjustment_history_data_bag: PatentTermAdjustmentHistoryDataBag) -> None:
        self.a_delay_quantity = a_delay_quantity
        self.b_delay_quantity = b_delay_quantity
        self.c_delay_quantity = c_delay_quantity
        self.overlapping_day_quantity = overlapping_day_quantity
        self.non_overlapping_day_quantity = non_overlapping_day_quantity
        self.ip_office_day_delay_quantity = ip_office_day_delay_quantity
        self.applicant_day_delay_quantity = applicant_day_delay_quantity
        self.adjustment_total_quantity = adjustment_total_quantity
        self.patent_term_adjustment_history_data_bag = patent_term_adjustment_history_data_bag


class PatentTermDataBag:
    mx_source: str
    mx_synced_date: str
    patent_term_adjustment_data: PatentTermAdjustmentData

    def __init__(self, mx_source: str, mx_synced_date: str, patent_term_adjustment_data: PatentTermAdjustmentData) -> None:
        self.mx_source = mx_source
        self.mx_synced_date = mx_synced_date
        self.patent_term_adjustment_data = patent_term_adjustment_data


class ProsecutionHistoryDatum:
    document_category: str
    document_code: str
    document_description: str
    document_handle: str
    file_name: str
    mail_room_date: datetime
    pages: int

    def __init__(self, document_category: str, document_code: str, document_description: str, document_handle: str, file_name: str, mail_room_date: datetime, pages: int) -> None:
        self.document_category = document_category
        self.document_code = document_code
        self.document_description = document_description
        self.document_handle = document_handle
        self.file_name = file_name
        self.mail_room_date = mail_room_date
        self.pages = pages


class ProsecutionHistoryDataBag:
    mx_source: str
    mx_synced_date: str
    prosecution_history_data: List[ProsecutionHistoryDatum]

    def __init__(self, mx_source: str, mx_synced_date: str, prosecution_history_data: List[ProsecutionHistoryDatum]) -> None:
        self.mx_source = mx_source
        self.mx_synced_date = mx_synced_date
        self.prosecution_history_data = prosecution_history_data


class TransactionHistoryDatum:
    event_date: datetime
    event_code: str
    event_description_text: str

    def __init__(self, event_date: datetime, event_code: str, event_description_text: str) -> None:
        self.event_date = event_date
        self.event_code = event_code
        self.event_description_text = event_description_text


class TransactionHistoryDataBag:
    mx_source: str
    mx_synced_date: str
    transaction_history_data: List[TransactionHistoryDatum]

    def __init__(self, mx_source: str, mx_synced_date: str, transaction_history_data: List[TransactionHistoryDatum]) -> None:
        self.mx_source = mx_source
        self.mx_synced_date = mx_synced_date
        self.transaction_history_data = transaction_history_data


class PatentData:
    patent_case_meta_data: PatentCaseMetaData
    transaction_history_data_bag: TransactionHistoryDataBag
    prosecution_history_data_bag: ProsecutionHistoryDataBag
    patent_term_data_bag: PatentTermDataBag
    foreign_priority_data_bag: ForeignPriorityDataBag
    continuity_data_bag: ContinuityDataBag
    attorney_information_data_bag: AttorneyInformationDataBag



class Patent:
    request_id: str
    client_request_handle: str
    identifier: str
    type: str
    patent_data: PatentData


