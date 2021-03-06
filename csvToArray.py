function csvToArray($file){
  $csv = file_get_contents($file);

  $newKeyArray = str_replace('"', '', $csv);
  $csv = str_replace(',', ';', $newKeyArray);
  $separatorCsv = ";";

  $row = explode("\n", $csv);
  $firstRow = trim($row[0]);
  $keys = explode($separatorCsv, $firstRow);
  $fileLines=file($file);
  $countLines = count($fileLines);
  $array = [];
  for ($i=1; $i <= $countLines-1; $i++) { 
    $secondRow = $row[$i];
    $values = explode($separatorCsv, $secondRow);
    $array[] = array_combine($keys, $values);
  }
  return $array;
}
