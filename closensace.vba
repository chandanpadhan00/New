Sub SaveAndCloseAllWorkbooks()
    Dim thisWB As Workbook
    Dim wb As Workbook
    Dim names() As String
    Dim i As Long, n As Long

    Set thisWB = ThisWorkbook ' workbook that holds the macro

    ' Collect names first (don’t close while iterating the collection)
    ReDim names(1 To Application.Workbooks.Count)
    i = 0
    For Each wb In Application.Workbooks
        If wb.Name <> thisWB.Name Then
            i = i + 1
            names(i) = wb.Name
        End If
    Next wb

    Application.DisplayAlerts = False  ' suppress format prompts

    ' Close all others
    For n = 1 To i
        With Workbooks(names(n))
            ' If it's a brand-new unsaved book, give it a quick name in Downloads
            If .Path = "" Then
                On Error Resume Next
                .SaveAs Filename:=Environ$("USERPROFILE") & "\Downloads\" & _
                                Replace(.Name, ".xls", "") & "_" & Format(Now, "yyyymmdd_hhnnss") & ".xlsx", _
                                FileFormat:=xlOpenXMLWorkbook
                On Error GoTo 0
            Else
                .Save
            End If
            .Close SaveChanges:=False
        End With
    Next n

    ' Finally close the macro workbook itself
    thisWB.Save
    thisWB.Close SaveChanges:=False

    Application.Quit
    Application.DisplayAlerts = True
End Sub