

/*
 * func:
 * 	cmpl	$1,  %edi                // compare long (double word), %edi - 1
 * 	jle     .L3		         // jump on less than or equal ( <= 0)
 *	pushq 	%rbx                     // save rbx (callee saved)
 *	leal    (%rdi, %rdi, 2),  %ebx   // %ebx <- 2 * %rdi + %rdi
 *	leal    3(%rdi),  %edx           // %edx <- 3 + %rdi
 *	testl   %edi,  %edi              // %edi & %edi
 *	cmovns  %edi,  %edx              // mov on non-negative ~SF, if %edi >= 0 then %edx <- %edi
 *	sarl    $2,   %edx    		 // %edx <- %edx >> 2       SAR; arithmetic right shift. SHR logical right shift.
 *	movl    %edx,  %edi		 // %edi <- %edx
 *	call    func			
 *	addl    %ebx,  %eax		 
 *	popq    %rbx                     // restore rbx
 *	ret
 *
 * .L3:
 * 	movl   $1,  %eax
 * 	ret
 * 
**/


int func(int n) {
	if (n <= 1) {
		return 1;
	}
	return 3 * n + func(n / 4);
}


int main(int argc, char **argv) {
	
	return func(10);
}
