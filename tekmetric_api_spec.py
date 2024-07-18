
API_SPEC_YAML = '''
openapi: 3.1.0
info:
  title: Tekmetric Customer API
  version: 1.0.0
servers:
- url: https://sandbox.tekmetric.com/api/v1
  description: Development server
paths:
  /customers:
    get:
      summary: API for fetching Tekmetric customer information
      parameters:
      - name: shop
        in: query
        description: Specify the shop ID to shop at. This parameter is REQUIRED in all customer queries to access the customer data from the desired shop.
        required: true
        schema:
          type: integer
          default: 1
      - name: search
        in: query
        description: A query that matches customer information by name, email, or phone number. If the user mentions a phone number, the query must be as specific as possible to the phone number mentioned by the user in its singular form, and don't contain any clarifiers like closest or similar.
        required: false
        schema:
          type: string
      - name: okForMarketing
        in: query
        description: A query that filters customers who are okay for marketing.
        required: false
        schema:
          type: boolean
      - name: updatedDateStart
        in: query
        description: A query for customers that were updated after the user provided date.
        required: false
        schema:
          type: string
          format: date-time
          example: 2019-02-27T10:31:59Z
      - name: updatedDateEnd
        in: query
        description: A query for customers that were updated before the user provided date.
        required: false
        schema:
          type: string
          format: date-time
          example: 2019-02-27T10:31:59Z
      - name: deletedDateStart
        in: query
        description: A query for customers that were deleted before the user provided date.
        required: false
        schema:
          type: string
          format: date-time
          example: 2019-02-27T10:31:59Z
      - name: deletedDateEnd
        in: query
        description: A query for customers that were deleted after the user provided date.
        required: false
        schema:
          type: string
          format: date-time
          example: 2019-02-27T10:31:59Z
      - name: sort
        in: query
        description: User will specify the property to sort on. You can specify multiple sort parameters i.e. "lastName,firstName".  Permitted Values include lastName, firstName, email.
        required: false
        schema:
          type: string
      - name: customerTypeId
        in: query
        description: Search by Customer type. The only permitted values are 1, for Person, or 2, for Business.
        required: false
        schema:
          type: integer
      - name: sortDirection
        in: query
        description: This defines the direction the user wants to sort their results. This must be used in conjunction with the "sort" parameter. The only permitted values are ASC or DESC.
        required: false
        schema:
          type: integer
          default: ASC
          enum:
          - ASC
          - DESC
      - name: size
        in: query
        description: A query that specifies the maximum number of results the user would like returned. The maximum page size is 100. For values greater than this value, the API will override and return 100 records. You can use pagination to access the next records.
        required: false
        schema:
          type: integer
      - name: page
        in: query
        description: A query that specifies the page number of the results you would like returned. This can be used in conjunction with the "size" parameter to view results beyond the maximum 100 number of results per page when necessary.
        required: false
        schema:
          type: integer
      responses:
        '200':
          description: Customer(s) found
          content:
            application/json:
              schema:
                $ref: #/components/schemas/CustomerResponse
        '503':
          description: one or more services are unavailable
components:
  schemas:
    CustomerResponse:
      type: object
      properties:
        content:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 35680
              firstName:
                type: string
                example: Vince
              lastName:
                type: string
                example: Zulauf
              email:
                type: string
                format: email
                example: vincezulauf@mail.test
              phone:
                type: array
                items:
                  type: object
                  properties:
                    number:
                      type: string
                      example: 111-111-1111
                    type:
                      type: string
                      example: Cell
                    primary:
                      type: boolean
                      example: true
              customerType:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  code:
                    type: string
                    example: PERSON
                  name:
                    type: string
                    example: Person
              contactFirstName:
                type: string
                nullable: true
                example: null
              contactLastName:
                type: string
                nullable: true
                example: null
              address:
                type: object
                properties:
                  address1:
                    type: string
                    example: 5103 Swift Park
                  address2:
                    type: string
                    nullable: true
                    example: null
                  city:
                    type: string
                    example: Tyreseview
                  state:
                    type: string
                    example: VT
                  zip:
                    type: string
                    example: 48824
                  streetAddress:
                    type: string
                    example: 5103 Swift Park
                  fullAddress:
                    type: string
                    example: 5103 Swift Park, Tyreseview, VT 48824
              shopId:
                type: integer
                example: 79
              okForMarketing:
                type: boolean
                example: true
              createdDate:
                type: string
                format: date-time
                example: 2019-02-27T10:31:59Z
              updatedDate:
                type: string
                format: date-time
                example: 2019-02-28T10:32:28Z
              deletedDate:
                type: string
                format: date-time
                example: 2019-02-28T10:32:28Z
        totalPages:
          type: integer
          example: 458
        last:
          type: boolean
          example: false
        totalElements:
          type: integer
          example: 4571
        sort:
          type: array
          items:
            type: object
            properties:
              direction:
                type: string
                example: DESC
              property:
                type: string
                example: firstName
              ignoreCase:
                type: boolean
                example: false
              nullHandling:
                type: string
                example: NATIVE
              ascending:
                type: boolean
                example: false
              descending:
                type: boolean
                example: true
        numberOfElements:
          type: integer
          example: 1
        first:
          type: boolean
          example: true
        size:
          type: integer
          example: 1
        number:
          type: integer
          example: 0
'''
