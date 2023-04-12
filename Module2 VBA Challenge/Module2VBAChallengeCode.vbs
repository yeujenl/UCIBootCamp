Sub TestCode():

'Defining worksheet'
For Each ws In Worksheets


'Creating new column titles'
ws.Cells(1, 9) = "Ticker"
ws.Cells(1, 10) = "Yearly Change"
ws.Cells(1, 11) = "Percentage Change"
ws.Cells(1, 12) = "Total Stock Volume"
ws.Cells(2, 15) = "Greatest % Increase"
ws.Cells(3, 15) = "Greatest % Decrease"
ws.Cells(4, 15) = "Greatest Total Volume"
ws.Cells(1, 16) = "Ticker"
ws.Cells(1, 17) = "Value"


'Dimensions'
Dim TickerName As String
Dim TickerRow As Double
Dim Run As Double
Dim OpeningValue As Double
Dim YearEndValue As Double
Dim YearlyChange As Double
Dim PercentageChange As Double
Dim TotalStock As LongPtr
Dim LastRow As Long


'Count to last row of current worksheet'
LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row


'Defining TickerRow to determine beginning row for cell writing'
TickerRow = 1
Run = 0
TotalStock = 0


'Assigning variable for first loop'
For i = 2 To LastRow


'If function when no change in Ticker Name'
If ws.Cells(i + 1, 1) = ws.Cells(i, 1) Then
    'Count number of rows in which the TickerName is the same'
    Run = Run + 1
    
    'Adding Total Stock Volume for TickerName that are the same'
    TotalStock = TotalStock + ws.Cells(i, 7)
    
'If function for change in Ticker Name'
ElseIf ws.Cells(i + 1, 1) <> ws.Cells(i, 1) Then

    'Defining TickerName'
    TickerName = ws.Cells(i, 1)
    
    'Changing row to write result as TickerName changes'
    TickerRow = TickerRow + 1
                  
    'Write TickerName to cell'
    ws.Cells(TickerRow, 9) = TickerName
    
    'Subtract number of rows run where TickerName is the same to pull the year opening stock price'
    OpeningValue = ws.Cells(i - Run, 3)
    
    'Defining end of year stock price'
    YearEndValue = ws.Cells(i, 6)
    
    'Calculating the difference between OpeningValue and YearEndValue to show yearly change'
    YearlyChange = YearEndValue - OpeningValue
    
    'Calulating percentage change'
    PercentageChange = YearlyChange / OpeningValue
    
    'Defining Total Stock Volume'
    TotalStock = TotalStock + ws.Cells(i, 7)
    
        
    'Writing Yearly Change, Percentage Change and Total Stock Volume result to cell'
    ws.Cells(TickerRow, 10) = YearlyChange
    ws.Cells(TickerRow, 11) = PercentageChange
    ws.Cells(TickerRow, 12) = TotalStock
        
        'Auto-fill cell with green color if Yearly Change is positive'
        If YearlyChange >= 0 Then
            ws.Cells(TickerRow, 10).Interior.ColorIndex = 4
        
        'Auto-fill cell with red color if Yearly Change is negative'
        Else:
            ws.Cells(TickerRow, 10).Interior.ColorIndex = 3
        
        End If
    
    'Format Percentage Change column to percentage'
    ws.Cells(TickerRow, 11).NumberFormat = "0.00%"
    
    'Resetting rows run due to change in TickerName'
    Run = 0
    
    'Reseting Total Stock Volume as TickerName changes'
    TotalStock = 0
    

End If

Next i


'Determining and writing the greatest percentage increase and format cell to percentage'
ws.Cells(2, 17) = WorksheetFunction.Max(ws.Range("K2:K" & LastRow))
ws.Cells(2, 17).NumberFormat = "0.00%"

'Determining and writing the greatest percentage decrease and format cell to percentage'
ws.Cells(3, 17) = WorksheetFunction.Min(ws.Range("K2:K" & LastRow))
ws.Cells(3, 17).NumberFormat = "0.00%"

'Determining and writing the greatest Total Stock Volume'
ws.Cells(4, 17) = WorksheetFunction.Max(ws.Range("L2:L" & LastRow))


'Second Iteration to fill in Ticker Name based on greatest percentage increase, percentage decrease and total stock volume'
'Assigning variable for 2nd loop'
For j = 2 To LastRow

'If function to match greatest percentage increase to Ticker Name'
If ws.Cells(j, 11) = ws.Cells(2, 17) Then
    ws.Cells(2, 16) = ws.Cells(j, 9)

End If

'If function to match greatest percentage decrease to Ticker Name'
If ws.Cells(j, 11) = ws.Cells(3, 17) Then
    ws.Cells(3, 16) = ws.Cells(j, 9)

End If

'If function to match greatest total stock volume to Ticker Name'
If ws.Cells(j, 12) = ws.Cells(4, 17) Then
    ws.Cells(4, 16) = ws.Cells(j, 9)

End If

Next j


'Format column to auto fit data'
ws.Cells.EntireColumn.AutoFit


Next ws

End Sub


