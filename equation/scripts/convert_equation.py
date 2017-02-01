<OMOBJ xmlns='http://www.openmath.org/OpenMath' version='2.0' cdbase='http://www.openmath.org/cd'>
	<OMA>
		<OMS cd='arith1' name='plus'/>
		<OMV name='a'/>
		<OMA>
			<OMS cd='arith1' name='power'/>
			<OMV name='b'/>
			<OMA style='invisible'>
				<OMS cd='arith1' name='times'/>
				<OMI>2</OMI>
				<OMA>
					<OMS cd='transc1' name='cos'/>
					<OMI>2</OMI>
				</OMA>
			</OMA>
		</OMA>
	</OMA>
</OMOBJ>


<OMOBJ xmlns='http://www.openmath.org/OpenMath' version='2.0' cdbase='http://www.openmath.org/cd'>
	<OMA>
		<OMS cd='arith1' name='plus'/>
		<OMA>
			<OMS cd='arith1' name='minus'/>
			<OMA>
			<OMS cd='arith1' name='plus'/>
			<OMA style='mfrac'>
			<OMS cd='arith1' name='divide'/>
			<OMV name='x'/>
			<OMI>2</OMI>
			</OMA>
			<OMA>
			<OMS cd='arith1' name='times'/>
			<OMI>45</OMI>
			<OMA>
			<OMS cd='transc1' name='cos'/>
			<OMI>45</OMI>
			</OMA>
			</OMA>
			</OMA>
			<OMA>
			<OMS cd='arith1' name='root'/>
			<OMI>7</OMI>
			<OMI>2</OMI>
			</OMA>
			</OMA>
			<OMA>
			<OMS cd='calculus1' name='int'/>
			<OMBIND>
				<OMS cd='fns1' name='lambda'/>
				<OMBVAR>
					<OMV name='x'/>
				</OMBVAR>
				<OMA>
					<OMS cd='arith1' name='power'/>
					<OMV name='x'/>
				<OMI>3</OMI>
				</OMA>
			</OMBIND>
		</OMA>
	</OMA>
</OMOBJ>