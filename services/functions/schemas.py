INPUT = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "openapi": {
      "type": "string"
    },
    "info": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "contact": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "email",
            "url"
          ]
        },
        "description": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "version",
        "contact",
        "description"
      ]
    },
    "paths": {
      "type": "object",
      "properties": {
        "/test": {
          "type": "object",
          "properties": {
            "parameters": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "$ref": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "$ref"
                  ]
                }
              ]
            },
            "get": {
              "type": "object",
              "properties": {
                "responses": {
                  "type": "object",
                  "properties": {
                    "200": {
                      "type": "object",
                      "properties": {
                        "description": {
                          "type": "string"
                        },
                        "content": {
                          "type": "object",
                          "properties": {
                            "text/plain": {
                              "type": "object",
                              "properties": {
                                "schema": {
                                  "type": "object",
                                  "properties": {
                                    "type": {
                                      "type": "string"
                                    },
                                    "example": {
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "type",
                                    "example"
                                  ]
                                }
                              },
                              "required": [
                                "schema"
                              ]
                            }
                          },
                          "required": [
                            "text/plain"
                          ]
                        }
                      },
                      "required": [
                        "description",
                        "content"
                      ]
                    }
                  },
                  "required": [
                    "200"
                  ]
                }
              },
              "required": [
                "responses"
              ]
            }
          },
          "required": [
            "parameters",
            "get"
          ]
        }
      },
      "required": [
        "/test"
      ]
    },
    "components": {
      "type": "object",
      "properties": {
        "parameters": {
          "type": "object",
          "properties": {
            "x-nd-meta-data": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "in": {
                  "type": "string"
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "example": {
                      "type": "string"
                    },
                    "minLength": {
                      "type": "integer"
                    },
                    "pattern": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "example",
                    "minLength",
                    "pattern"
                  ]
                },
                "description": {
                  "type": "string"
                },
                "required": {
                  "type": "boolean"
                }
              },
              "required": [
                "name",
                "in",
                "schema",
                "description",
                "required"
              ]
            }
          },
          "required": [
            "x-nd-meta-data"
          ]
        }
      },
      "required": [
        "parameters"
      ]
    }
  },
  "required": [
    "openapi",
    "info",
    "paths",
    "components"
  ]
}

OUTPUT = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Sample outgoing schema",
    "description": "The root schema comprises the entire JSON document.",
    "examples": [{"statusCode": 200, "body": "response"}],
    "required": ["statusCode", "body"],
    "properties": {
        "statusCode": {"$id": "#/properties/statusCode", "type": "integer", "title": "The statusCode"},
        "body": {"$id": "#/properties/body", "type": "string", "title": "The response"},
    },
}