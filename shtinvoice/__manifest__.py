{
    "name": "SHTInvoice",
    "version":"1.0",
    "author":"Prisms - SHT",
    "description":"This App for SHT invoice",
    "sequence":-100,
    "depends":["base","product"],
    "data":["views/sht_delivery.xml",
            "views/sht_invoice_views.xml",
            "security/ir.model.access.csv",
            "report/report.xml",
            "report/delivery_report.xml",
            "report/packing_report.xml",
            "report/proforma_report.xml"
            ],
    "installable":True,
    "application":True
}